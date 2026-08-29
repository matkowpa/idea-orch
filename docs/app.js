const REPO = "matkowpa/idea-orch";
const BRANCH = "main";
const $ = (id) => document.getElementById(id);

function slugify(text) {
  const map = {a:"ą",c:"ć",e:"ę",l:"ł",n:"ń",o:"ó",s:"ś",z:"ż",x:"ź"};
  return text.toLowerCase()
    .replace(/[ąćęłńóśżź]/g, (ch) => {
      for (const [k, v] of Object.entries(map)) if (v === ch) return k;
      return ch;
    })
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 48) || "pomysl";
}

function headers(pat) {
  return { "Authorization": "Bearer " + pat, "Accept": "application/vnd.github+json" };
}

async function getFileSha(path, pat) {
  const r = await fetch(`https://api.github.com/repos/${REPO}/contents/${path}?ref=${BRANCH}`, { headers: headers(pat) });
  if (r.status === 404) return null;
  if (!r.ok) throw new Error("GitHub API: " + r.status);
  return (await r.json()).sha;
}

async function putFile(path, content, message, pat) {
  const body = { message, content: btoa(unescape(encodeURIComponent(content))), branch: BRANCH };
  const sha = await getFileSha(path, pat);
  if (sha) body.sha = sha;
  const r = await fetch(`https://api.github.com/repos/${REPO}/contents/${path}`, {
    method: "PUT", headers: headers(pat), body: JSON.stringify(body)
  });
  if (!r.ok) throw new Error("Zapis pliku nie powiódł się: " + r.status + " " + (await r.text()).slice(0, 200));
}

async function dispatchRun(slug, pat) {
  const r = await fetch(`https://api.github.com/repos/${REPO}/actions/workflows/run-boardroom.yml/dispatches`, {
    method: "POST", headers: { ...headers(pat), "Content-Type": "application/json" },
    body: JSON.stringify({ ref: BRANCH, inputs: { slug } })
  });
  if (r.status !== 204) throw new Error("Dispatch nie powiódł się: " + r.status + " " + (await r.text()).slice(0, 200));
}

async function pollResult(slug, pat, onTick) {
  const url = `https://raw.githubusercontent.com/${REPO}/${BRANCH}/sessions/${slug}/concept.md`;
  const deadline = Date.now() + 10 * 60 * 1000; // 10 min
  while (Date.now() < deadline) {
    // postep debaty przez GitHub API (bez cache raw; PAT podnosi limit)
    try {
      const pr = await fetch(`https://api.github.com/repos/${REPO}/contents/sessions/${slug}/_progress.json?ref=${BRANCH}&t=` + Date.now(), { headers: headers(pat) });
      if (pr.ok) {
        const jj = await pr.json();
        const j = JSON.parse(decodeURIComponent(escape(atob(jj.content.replace(/\s/g, "")))));
        const label = `${j.stage}${j.detail ? " — " + j.detail : ""}`;
        setProgress(j.step, j.total, `Etap ${j.step}/${j.total}: ${label}`);
        onTick(`Etap ${j.step}/${j.total}: ${label}`);
      }
    } catch (e) { /* progres niedostepny — pomijamy */ }
    const r = await fetch(`https://api.github.com/repos/${REPO}/contents/sessions/${slug}/concept.md?ref=${BRANCH}&t=` + Date.now(), { headers: headers(pat) });
    if (r.ok) {
      const jj = await r.json();
      return decodeURIComponent(escape(atob(jj.content.replace(/\s/g, ""))));
    }
    await new Promise((res) => setTimeout(res, 10000));
  }
  throw new Error("Timeout — sprawdź log Action: https://github.com/" + REPO + "/actions");
}

function setStatus(msg) { $("status").textContent = msg; }

function setProgress(step, total, label) {
  const wrap = $("progress-wrap"), bar = $("progress-bar"), lab = $("progress-label");
  if (step == null) { wrap.hidden = true; lab.hidden = true; return; }
  wrap.hidden = false; lab.hidden = false;
  bar.style.width = Math.min(100, Math.round((step / total) * 100)) + "%";
  lab.textContent = label || ("Etap " + step + "/" + total);
}

$("file").addEventListener("change", (e) => {
  const f = e.target.files[0];
  if (!f) return;
  const reader = new FileReader();
  reader.onload = () => { $("idea").value = reader.result; };
  reader.readAsText(f);
});

$("run").addEventListener("click", async () => {
  const idea = $("idea").value.trim();
  const pat = $("pat").value.trim();
  if (!idea) { alert("Wpisz pomysł."); return; }
  if (!pat) { alert("Wklej GitHub PAT."); return; }
  sessionStorage.setItem("gh_pat", pat);

  const slug = slugify($("slug").value.trim() || idea.slice(0, 60));
  $("run").disabled = true;
  try {
    setStatus("Zapisuję pomysł do queue/" + slug + ".md ...");
    await putFile("queue/" + slug + ".md", idea, "Pomysł: " + slug, pat);
    setStatus("Uruchamiam workflow ...");
    setProgress(1, 10, "Start debaty");
    await dispatchRun(slug, pat);
    setStatus("Debata trwa — odpytuję o postęp co 10 s ...");
    const md = await pollResult(slug, pat, () => setStatus("Debata trwa ... odpytuję co 10 s"));
    $("result").innerHTML = marked.parse(md);
    $("artifacts-link").innerHTML =
      'Pełne artefakty: <a target="_blank" href="https://github.com/' + REPO + '/tree/' + BRANCH + '/sessions/' + slug + '">sessions/' + slug + '</a>';
    $("result-section").hidden = false;
    setProgress(10, 10, "Gotowe");
    setStatus("Gotowe.");
  } catch (err) {
    setStatus("Błąd: " + err.message);
    setProgress(null);
  } finally {
    $("run").disabled = false;
  }
});

const savedPat = sessionStorage.getItem("gh_pat");
if (savedPat) $("pat").value = savedPat;
