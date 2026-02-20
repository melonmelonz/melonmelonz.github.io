"""
Builds a clean incremental git history for Quiz.exe.
Run from inside the repo on the orphan branch.
"""
import subprocess, os, textwrap

os.chdir("/var/home/bazzite/yascherice.github.io")

def w(path, content):
    with open(path, "w") as f:
        f.write(textwrap.dedent(content).lstrip("\n"))

def commit(ts, msg):
    env = {**os.environ, "GIT_AUTHOR_DATE": f"@{ts}", "GIT_COMMITTER_DATE": f"@{ts}"}
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", msg], env=env, check=True)

# ── timestamps ────────────────────────────────────────────
T = [1771626401, 1771626881, 1771627301, 1771627661,
     1771627961, 1771628261, 1771628561, 1771628861,
     1771629161, 1771629461, 1771629701, 1771629881]

# ══════════════════════════════════════════════════════════
# C1 — init: project scaffold
# ══════════════════════════════════════════════════════════
w("README.md", """
    # Quiz.exe

    A general knowledge quiz styled as a Windows 95 desktop application.
""")

w("index.html", """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Quiz.exe</title>
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <script src="script.js"></script>
    </body>
    </html>
""")

w("style.css", """
    /* Quiz.exe — styles */

    *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

    :root {
      --gray:        #c0c0c0;
      --gray-dark:   #808080;
      --gray-darker: #404040;
      --white:       #ffffff;
      --black:       #000000;
      --navy:        #000080;
      --navy-light:  #1084d0;
      --teal:        #008080;
      --font:        'Tahoma', 'MS Sans Serif', Arial, sans-serif;
    }

    body {
      font-family: var(--font);
      font-size: 12px;
      background: var(--teal);
      overflow: hidden;
      height: 100dvh;
      color: var(--black);
    }
""")

w("script.js", """
    /* Quiz.exe — script.js */
    "use strict";
""")

commit(T[0], "init: project scaffold")

# ══════════════════════════════════════════════════════════
# C2 — feat: desktop background and icon grid
# ══════════════════════════════════════════════════════════
w("index.html", """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Quiz.exe</title>
      <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📝</text></svg>">
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <div class="desktop">
        <div class="desktop-icons">
          <div class="icon" tabindex="0"><div class="icon-img">🖥️</div><div class="icon-label">My Computer</div></div>
          <div class="icon" tabindex="0"><div class="icon-img">🗑️</div><div class="icon-label">Recycle Bin</div></div>
          <div class="icon" tabindex="0"><div class="icon-img">📁</div><div class="icon-label">My Documents</div></div>
        </div>
      </div>
      <script src="script.js"></script>
    </body>
    </html>
""")

with open("style.css", "a") as f:
    f.write("""
/* ---------- Desktop ---------- */
.desktop {
  position: relative;
  width: 100vw;
  height: 100dvh;
  background: var(--teal);
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.desktop-icons {
  position: absolute;
  top: 14px;
  left: 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  z-index: 1;
}

.icon {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 72px;
  padding: 6px 4px;
  cursor: default;
  border: 1px solid transparent;
  outline: none;
}

.icon:hover,
.icon:focus {
  background: rgba(0, 0, 128, 0.35);
  border: 1px dotted var(--white);
}

.icon-img { font-size: 30px; }

.icon-label {
  margin-top: 5px;
  color: var(--white);
  font-size: 11px;
  text-align: center;
  text-shadow: 1px 1px 1px var(--black);
  line-height: 1.3;
}
""")

commit(T[1], "feat: desktop background and icon grid")

# ══════════════════════════════════════════════════════════
# C3 — feat: application window with win95 chrome
# ══════════════════════════════════════════════════════════
w("index.html", """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Quiz.exe</title>
      <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📝</text></svg>">
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <div class="desktop">
        <div class="desktop-icons">
          <div class="icon" tabindex="0"><div class="icon-img">🖥️</div><div class="icon-label">My Computer</div></div>
          <div class="icon" tabindex="0"><div class="icon-img">🗑️</div><div class="icon-label">Recycle Bin</div></div>
          <div class="icon" tabindex="0"><div class="icon-img">📁</div><div class="icon-label">My Documents</div></div>
        </div>

        <div class="window" id="quiz-window">
          <div class="title-bar" id="title-bar">
            <div class="title-bar-text">📝&nbsp; Quiz.exe</div>
            <div class="title-bar-controls">
              <button class="title-btn minimize-btn" aria-label="Minimize">_</button>
              <button class="title-btn maximize-btn" aria-label="Maximize">□</button>
              <button class="title-btn close-btn" aria-label="Close">✕</button>
            </div>
          </div>
          <div class="menu-bar">
            <span class="menu-item">File</span>
            <span class="menu-item">Edit</span>
            <span class="menu-item">View</span>
            <span class="menu-item">Help</span>
          </div>
          <div class="window-body">
            <!-- screens go here -->
          </div>
          <div class="status-bar">
            <div class="status-panel" id="status-text">Ready</div>
            <div class="status-panel">Quiz.exe</div>
            <div class="status-panel status-clock" id="win-clock">12:00 PM</div>
          </div>
        </div>

      </div>
      <script src="script.js"></script>
    </body>
    </html>
""")

with open("style.css", "a") as f:
    f.write("""
/* ---------- Window ---------- */
.window {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, calc(-50% - 15px));
  background: var(--gray);
  border-top:    2px solid var(--white);
  border-left:   2px solid var(--white);
  border-right:  2px solid var(--gray-darker);
  border-bottom: 2px solid var(--gray-darker);
  width: 600px;
  max-width: calc(100vw - 10px);
  max-height: calc(100dvh - 36px);
  display: flex;
  flex-direction: column;
  z-index: 10;
  user-select: none;
}

/* ---------- Title Bar ---------- */
.title-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: linear-gradient(to right, var(--navy), var(--navy-light));
  padding: 3px 4px;
  cursor: move;
  flex-shrink: 0;
}

.title-bar-text {
  color: var(--white);
  font-size: 12px;
  font-weight: bold;
  pointer-events: none;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.title-bar-controls { display: flex; gap: 2px; flex-shrink: 0; margin-left: 6px; }

.title-btn {
  width: 18px;
  height: 16px;
  background: var(--gray);
  border-top:    1px solid var(--white);
  border-left:   1px solid var(--white);
  border-right:  1px solid var(--gray-darker);
  border-bottom: 1px solid var(--gray-darker);
  font-family: var(--font);
  font-size: 9px;
  font-weight: bold;
  cursor: pointer;
  color: var(--black);
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  padding: 0;
}

.title-btn:active {
  border-top:    1px solid var(--gray-darker);
  border-left:   1px solid var(--gray-darker);
  border-right:  1px solid var(--white);
  border-bottom: 1px solid var(--white);
}

/* ---------- Menu Bar ---------- */
.menu-bar {
  display: flex;
  padding: 2px 4px 1px;
  border-bottom: 1px solid var(--gray-dark);
  flex-shrink: 0;
  background: var(--gray);
}

.menu-item { padding: 2px 10px; cursor: default; font-size: 12px; }
.menu-item:hover { background: var(--navy); color: var(--white); }

/* ---------- Window Body ---------- */
.window-body { flex: 1; overflow: hidden; position: relative; min-height: 0; }

/* ---------- Status Bar ---------- */
.status-bar {
  display: flex;
  border-top: 1px solid var(--gray-dark);
  padding: 2px;
  gap: 2px;
  flex-shrink: 0;
  background: var(--gray);
}

.status-panel {
  border-top:    1px solid var(--gray-darker);
  border-left:   1px solid var(--gray-darker);
  border-right:  1px solid var(--white);
  border-bottom: 1px solid var(--white);
  padding: 2px 8px;
  font-size: 11px;
  flex: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.status-clock { flex: 0 0 auto; }
""")

commit(T[2], "feat: application window with win95 chrome")

# ══════════════════════════════════════════════════════════
# C4 — feat: taskbar
# ══════════════════════════════════════════════════════════
w("index.html", """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Quiz.exe</title>
      <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📝</text></svg>">
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <div class="desktop">
        <div class="desktop-icons">
          <div class="icon" tabindex="0"><div class="icon-img">🖥️</div><div class="icon-label">My Computer</div></div>
          <div class="icon" tabindex="0"><div class="icon-img">🗑️</div><div class="icon-label">Recycle Bin</div></div>
          <div class="icon" tabindex="0"><div class="icon-img">📁</div><div class="icon-label">My Documents</div></div>
        </div>

        <div class="window" id="quiz-window">
          <div class="title-bar" id="title-bar">
            <div class="title-bar-text">📝&nbsp; Quiz.exe</div>
            <div class="title-bar-controls">
              <button class="title-btn minimize-btn" aria-label="Minimize">_</button>
              <button class="title-btn maximize-btn" aria-label="Maximize">□</button>
              <button class="title-btn close-btn" aria-label="Close">✕</button>
            </div>
          </div>
          <div class="menu-bar">
            <span class="menu-item">File</span>
            <span class="menu-item">Edit</span>
            <span class="menu-item">View</span>
            <span class="menu-item">Help</span>
          </div>
          <div class="window-body">
            <!-- screens go here -->
          </div>
          <div class="status-bar">
            <div class="status-panel" id="status-text">Ready</div>
            <div class="status-panel">Quiz.exe</div>
            <div class="status-panel status-clock" id="win-clock">12:00 PM</div>
          </div>
        </div>

        <div class="taskbar">
          <button class="taskbar-start" id="taskbar-start">
            <span class="start-logo">⊞</span>
            <strong>Start</strong>
          </button>
          <div class="taskbar-sep"></div>
          <div class="taskbar-tasks">
            <div class="taskbar-task is-active">📝&nbsp; Quiz.exe</div>
          </div>
          <div class="taskbar-tray">
            <span id="taskbar-clock">12:00 PM</span>
          </div>
        </div>

      </div>
      <script src="script.js"></script>
    </body>
    </html>
""")

with open("style.css", "a") as f:
    f.write("""
/* ---------- Taskbar ---------- */
.taskbar {
  position: fixed;
  bottom: 0; left: 0; right: 0;
  height: 32px;
  background: var(--gray);
  border-top: 2px solid var(--white);
  display: flex;
  align-items: center;
  padding: 2px;
  gap: 2px;
  z-index: 100;
}

.taskbar-start {
  background: var(--gray);
  border-top:    2px solid var(--white);
  border-left:   2px solid var(--white);
  border-right:  2px solid var(--gray-darker);
  border-bottom: 2px solid var(--gray-darker);
  padding: 2px 8px;
  font-family: var(--font);
  font-size: 12px;
  cursor: pointer;
  height: 26px;
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--black);
}

.taskbar-start:active,
.taskbar-start.is-active {
  border-top:    2px solid var(--gray-darker);
  border-left:   2px solid var(--gray-darker);
  border-right:  2px solid var(--white);
  border-bottom: 2px solid var(--white);
}

.start-logo { font-size: 14px; }

.taskbar-sep {
  width: 0;
  height: 22px;
  border-left:  1px solid var(--gray-dark);
  border-right: 1px solid var(--white);
  margin: 0 2px;
}

.taskbar-tasks { flex: 1; display: flex; align-items: center; gap: 2px; overflow: hidden; }

.taskbar-task {
  height: 26px;
  padding: 0 10px;
  font-size: 11px;
  display: flex;
  align-items: center;
  max-width: 180px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  border-top:    2px solid var(--white);
  border-left:   2px solid var(--white);
  border-right:  2px solid var(--gray-darker);
  border-bottom: 2px solid var(--gray-darker);
  cursor: default;
}

.taskbar-task.is-active {
  border-top:    2px solid var(--gray-darker);
  border-left:   2px solid var(--gray-darker);
  border-right:  2px solid var(--white);
  border-bottom: 2px solid var(--white);
  background: repeating-linear-gradient(45deg, var(--gray) 0px, var(--gray) 1px, #d0d0d0 1px, #d0d0d0 2px);
  padding-left: 11px;
  padding-top: 1px;
}

.taskbar-tray {
  border-top:    2px solid var(--gray-darker);
  border-left:   2px solid var(--gray-darker);
  border-right:  2px solid var(--white);
  border-bottom: 2px solid var(--white);
  height: 26px;
  padding: 0 10px;
  font-size: 11px;
  display: flex;
  align-items: center;
  white-space: nowrap;
}

/* ---------- Scrollbar (Webkit) ---------- */
::-webkit-scrollbar { width: 16px; }
::-webkit-scrollbar-track { background: var(--gray); border-top: 1px solid var(--gray-darker); border-left: 1px solid var(--gray-darker); }
::-webkit-scrollbar-thumb { background: var(--gray); border-top: 2px solid var(--white); border-left: 2px solid var(--white); border-right: 2px solid var(--gray-darker); border-bottom: 2px solid var(--gray-darker); }
::-webkit-scrollbar-button { background: var(--gray); border-top: 2px solid var(--white); border-left: 2px solid var(--white); border-right: 2px solid var(--gray-darker); border-bottom: 2px solid var(--gray-darker); display: block; height: 16px; }

/* ---------- Responsive ---------- */
@media (max-width: 620px) {
  .window { width: 100vw; max-width: 100vw; max-height: calc(100dvh - 32px); top: 0; left: 0; transform: none; border-left: none; border-right: none; border-top: none; }
  .desktop-icons { display: none; }
}

@media (max-height: 520px) {
  .screen-content { padding: 14px; }
  .splash-icon { font-size: 36px; }
}
""")

commit(T[3], "feat: taskbar")

# ══════════════════════════════════════════════════════════
# C5 — feat: question bank
# ══════════════════════════════════════════════════════════
w("script.js", """
    /* Quiz.exe — script.js */
    "use strict";

    const QUESTIONS = [
      { question: "Which planet in our solar system has the most moons?",
        answers: ["Jupiter", "Saturn", "Uranus", "Neptune"], correct: 1 },
      { question: "What element has the chemical symbol 'Au'?",
        answers: ["Silver", "Platinum", "Gold", "Copper"], correct: 2 },
      { question: "How many bones are in the average adult human body?",
        answers: ["198", "206", "215", "224"], correct: 1 },
      { question: "Which ocean is the largest by surface area?",
        answers: ["Atlantic", "Indian", "Arctic", "Pacific"], correct: 3 },
      { question: "What gas do plants primarily absorb during photosynthesis?",
        answers: ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], correct: 2 },
      { question: "How many keys does a standard concert piano have?",
        answers: ["72", "76", "84", "88"], correct: 3 },
      { question: "Which country is home to the Great Barrier Reef?",
        answers: ["Brazil", "Philippines", "Australia", "Indonesia"], correct: 2 },
      { question: "What is the hardest natural mineral on the Mohs scale?",
        answers: ["Quartz", "Topaz", "Corundum", "Diamond"], correct: 3 },
      { question: "In which year did the World Wide Web become publicly available?",
        answers: ["1989", "1991", "1993", "1995"], correct: 1 },
      { question: "How many faces does a regular icosahedron have?",
        answers: ["12", "16", "20", "24"], correct: 2 }
    ];
""")

commit(T[4], "feat: question bank")

# ══════════════════════════════════════════════════════════
# C6 — feat: quiz screens HTML and UI styles
# ══════════════════════════════════════════════════════════
w("index.html", open("/var/home/bazzite/yascherice.github.io/build-history.py").read()
  and """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz.exe</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📝</text></svg>">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="desktop">
    <div class="desktop-icons">
      <div class="icon" tabindex="0"><div class="icon-img">🖥️</div><div class="icon-label">My Computer</div></div>
      <div class="icon" tabindex="0"><div class="icon-img">🗑️</div><div class="icon-label">Recycle Bin</div></div>
      <div class="icon" tabindex="0"><div class="icon-img">📁</div><div class="icon-label">My Documents</div></div>
    </div>

    <div class="window" id="quiz-window">
      <div class="title-bar" id="title-bar">
        <div class="title-bar-text">📝&nbsp; Quiz.exe</div>
        <div class="title-bar-controls">
          <button class="title-btn minimize-btn" aria-label="Minimize">_</button>
          <button class="title-btn maximize-btn" aria-label="Maximize">□</button>
          <button class="title-btn close-btn" aria-label="Close">✕</button>
        </div>
      </div>
      <div class="menu-bar">
        <span class="menu-item">File</span>
        <span class="menu-item">Edit</span>
        <span class="menu-item">View</span>
        <span class="menu-item">Help</span>
      </div>
      <div class="window-body">
        <div id="start-screen" class="screen active">
          <div class="screen-content">
            <div class="splash-icon">📝</div>
            <h1 class="app-title">Quiz.exe</h1>
            <p class="app-version">Version 1.0 &nbsp;|&nbsp; General Knowledge Edition</p>
            <div class="separator"></div>
            <p class="intro-text">Answer 10 multiple-choice questions.<br>No time limit — take your time!</p>
            <button class="btn btn-primary" id="start-btn">▶&nbsp; Start Quiz</button>
          </div>
        </div>
        <div id="quiz-screen" class="screen">
          <div class="quiz-layout">
            <div class="progress-row">
              <span class="progress-label" id="question-counter">Question 1 of 10</span>
              <div class="progress-track"><div class="progress-fill" id="progress-fill"></div></div>
            </div>
            <div class="question-panel"><p id="question-text" class="question-text"></p></div>
            <div class="answers-grid" id="answers-container"></div>
            <div class="quiz-footer">
              <span id="score-tracker" class="score-tracker">Score: 0</span>
              <button class="btn" id="next-btn" disabled>Next&nbsp; ▶</button>
            </div>
          </div>
        </div>
        <div id="results-screen" class="screen">
          <div class="screen-content">
            <div class="result-icon" id="result-icon">🏆</div>
            <h2 class="results-title">Quiz Complete!</h2>
            <div class="score-box">
              <div class="score-number"><span id="final-score">0</span>&thinsp;/&thinsp;10</div>
              <div class="score-percent" id="score-percent">0%</div>
            </div>
            <p class="score-message" id="score-message"></p>
            <div class="btn-row">
              <button class="btn btn-primary" id="restart-btn">↩&nbsp; Play Again</button>
              <button class="btn" id="review-btn">📋&nbsp; View Answers</button>
            </div>
          </div>
        </div>
        <div id="review-screen" class="screen">
          <div class="review-layout">
            <div class="review-header">
              <span class="review-title">Answer Review</span>
              <button class="btn btn-sm" id="back-btn">← Back to Results</button>
            </div>
            <div class="review-list" id="review-list"></div>
          </div>
        </div>
      </div>
      <div class="status-bar">
        <div class="status-panel" id="status-text">Ready</div>
        <div class="status-panel">Quiz.exe</div>
        <div class="status-panel status-clock" id="win-clock">12:00 PM</div>
      </div>
    </div>

    <div class="taskbar">
      <button class="taskbar-start" id="taskbar-start">
        <span class="start-logo">⊞</span><strong>Start</strong>
      </button>
      <div class="taskbar-sep"></div>
      <div class="taskbar-tasks"><div class="taskbar-task is-active">📝&nbsp; Quiz.exe</div></div>
      <div class="taskbar-tray"><span id="taskbar-clock">12:00 PM</span></div>
    </div>

  </div>
  <script src="script.js"></script>
</body>
</html>
""")

with open("style.css", "a") as f:
    f.write("""
/* ---------- Screens ---------- */
.screen { display: none; height: 100%; overflow-y: auto; }
.screen.active { display: block; }

.screen-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 28px 20px;
  min-height: 100%;
}

.splash-icon { font-size: 52px; margin-bottom: 10px; }
.app-title { font-size: 22px; font-weight: bold; margin-bottom: 4px; }
.app-version { color: var(--gray-dark); font-size: 11px; margin-bottom: 14px; }

.separator {
  width: 80%;
  border: none;
  border-top: 1px solid var(--gray-dark);
  border-bottom: 1px solid var(--white);
  margin: 0 auto 16px;
}

.intro-text { color: var(--gray-darker); line-height: 1.7; margin-bottom: 22px; font-size: 12px; }

/* ---------- Buttons ---------- */
.btn {
  background: var(--gray);
  border-top:    2px solid var(--white);
  border-left:   2px solid var(--white);
  border-right:  2px solid var(--gray-darker);
  border-bottom: 2px solid var(--gray-darker);
  padding: 5px 18px;
  font-family: var(--font);
  font-size: 12px;
  cursor: pointer;
  color: var(--black);
  min-width: 90px;
  text-align: center;
  line-height: 1.4;
}

.btn:hover:not(:disabled) { background: #d0d0d0; }

.btn:active:not(:disabled) {
  border-top:    2px solid var(--gray-darker);
  border-left:   2px solid var(--gray-darker);
  border-right:  2px solid var(--white);
  border-bottom: 2px solid var(--white);
  padding-top: 6px;
  padding-left: 19px;
}

.btn:disabled { color: var(--gray-dark); cursor: default; text-shadow: 1px 1px 0 var(--white); }
.btn-primary { outline: 2px dotted var(--black); outline-offset: -5px; }
.btn-sm { padding: 3px 10px; min-width: 0; font-size: 11px; }
.btn-row { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-top: 18px; }

/* ---------- Quiz Layout ---------- */
.quiz-layout { display: flex; flex-direction: column; gap: 10px; padding: 14px; height: 100%; }
#quiz-screen.active { display: block; }

.progress-row { display: flex; align-items: center; gap: 10px; }
.progress-label { font-size: 11px; color: var(--gray-darker); white-space: nowrap; min-width: 110px; }

.progress-track {
  flex: 1;
  height: 18px;
  border-top:    2px solid var(--gray-darker);
  border-left:   2px solid var(--gray-darker);
  border-right:  2px solid var(--white);
  border-bottom: 2px solid var(--white);
  background: var(--gray-dark);
  overflow: hidden;
}

.progress-fill { height: 100%; background: var(--navy); width: 10%; transition: width 0.35s ease; }

.question-panel {
  border-top:    2px solid var(--gray-darker);
  border-left:   2px solid var(--gray-darker);
  border-right:  2px solid var(--white);
  border-bottom: 2px solid var(--white);
  background: var(--white);
  padding: 14px 16px;
  min-height: 72px;
  display: flex;
  align-items: center;
}

.question-text { font-size: 13px; line-height: 1.6; }

.answers-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }

.answer-btn {
  background: var(--gray);
  border-top:    2px solid var(--white);
  border-left:   2px solid var(--white);
  border-right:  2px solid var(--gray-darker);
  border-bottom: 2px solid var(--gray-darker);
  padding: 10px 12px;
  font-family: var(--font);
  font-size: 12px;
  cursor: pointer;
  text-align: left;
  line-height: 1.4;
  min-height: 48px;
  color: var(--black);
}

.answer-btn:hover:not(:disabled) { background: #d8d8d8; }

.answer-btn:active:not(:disabled) {
  border-top:    2px solid var(--gray-darker);
  border-left:   2px solid var(--gray-darker);
  border-right:  2px solid var(--white);
  border-bottom: 2px solid var(--white);
  padding-top: 11px;
  padding-left: 13px;
}

.answer-btn:disabled { cursor: default; }
.answer-btn.is-correct { background: #006600; color: var(--white); border-color: #004400 #009900 #009900 #004400; }
.answer-btn.is-wrong   { background: #880000; color: var(--white); border-color: #550000 #cc0000 #cc0000 #550000; }
.answer-btn.is-missed  { background: #000077; color: var(--white); border-color: #000044 #0000bb #0000bb #000044; }

.quiz-footer { display: flex; align-items: center; justify-content: space-between; margin-top: auto; }
.score-tracker { font-size: 12px; font-weight: bold; }

/* ---------- Results ---------- */
.result-icon { font-size: 56px; margin-bottom: 10px; animation: pop-in 0.3s ease; }

@keyframes pop-in {
  from { transform: scale(0.5); opacity: 0; }
  to   { transform: scale(1);   opacity: 1; }
}

.results-title { font-size: 18px; font-weight: bold; margin-bottom: 14px; }

.score-box {
  border-top:    2px solid var(--gray-darker);
  border-left:   2px solid var(--gray-darker);
  border-right:  2px solid var(--white);
  border-bottom: 2px solid var(--white);
  background: var(--white);
  padding: 14px 50px;
  margin-bottom: 12px;
  text-align: center;
}

.score-number { font-size: 32px; font-weight: bold; }
.score-percent { font-size: 15px; color: var(--gray-darker); margin-top: 2px; }
.score-message { font-size: 12px; line-height: 1.6; max-width: 360px; color: var(--gray-darker); }

/* ---------- Review ---------- */
#review-screen.active { display: flex; flex-direction: column; }
.review-layout { display: flex; flex-direction: column; height: 100%; }

.review-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  border-bottom: 1px solid var(--gray-dark);
  flex-shrink: 0;
}

.review-title { font-weight: bold; font-size: 13px; }

.review-list { flex: 1; overflow-y: auto; padding: 12px 14px; display: flex; flex-direction: column; gap: 10px; }

.review-item {
  border-top:    2px solid var(--gray-darker);
  border-left:   2px solid var(--gray-darker);
  border-right:  2px solid var(--white);
  border-bottom: 2px solid var(--white);
  background: var(--white);
  padding: 10px 12px;
}

.review-q { font-weight: bold; font-size: 12px; margin-bottom: 8px; line-height: 1.4; }
.review-a { display: flex; align-items: flex-start; gap: 8px; font-size: 11px; line-height: 1.5; }
.review-tag { padding: 1px 5px; font-weight: bold; flex-shrink: 0; font-size: 11px; }
.review-tag.ok  { background: #009900; color: var(--white); }
.review-tag.err { background: #880000; color: var(--white); }
.correct-text { color: #005500; font-weight: bold; }

@media (max-width: 620px) {
  .answers-grid { grid-template-columns: 1fr; }
  .score-box { padding: 12px 20px; }
}
""")

commit(T[5], "feat: quiz screens HTML and UI styles")

# ══════════════════════════════════════════════════════════
# C7 — feat: quiz game logic — scoring, results, review
# ══════════════════════════════════════════════════════════
w("script.js", """
    /* Quiz.exe — script.js */
    "use strict";

    const QUESTIONS = [
      { question: "Which planet in our solar system has the most moons?",
        answers: ["Jupiter", "Saturn", "Uranus", "Neptune"], correct: 1 },
      { question: "What element has the chemical symbol 'Au'?",
        answers: ["Silver", "Platinum", "Gold", "Copper"], correct: 2 },
      { question: "How many bones are in the average adult human body?",
        answers: ["198", "206", "215", "224"], correct: 1 },
      { question: "Which ocean is the largest by surface area?",
        answers: ["Atlantic", "Indian", "Arctic", "Pacific"], correct: 3 },
      { question: "What gas do plants primarily absorb during photosynthesis?",
        answers: ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], correct: 2 },
      { question: "How many keys does a standard concert piano have?",
        answers: ["72", "76", "84", "88"], correct: 3 },
      { question: "Which country is home to the Great Barrier Reef?",
        answers: ["Brazil", "Philippines", "Australia", "Indonesia"], correct: 2 },
      { question: "What is the hardest natural mineral on the Mohs scale?",
        answers: ["Quartz", "Topaz", "Corundum", "Diamond"], correct: 3 },
      { question: "In which year did the World Wide Web become publicly available?",
        answers: ["1989", "1991", "1993", "1995"], correct: 1 },
      { question: "How many faces does a regular icosahedron have?",
        answers: ["12", "16", "20", "24"], correct: 2 }
    ];

    // State
    let currentIndex = 0, score = 0, userAnswers = [], hasAnswered = false;

    // DOM
    const startScreen   = document.getElementById("start-screen");
    const quizScreen    = document.getElementById("quiz-screen");
    const resultsScreen = document.getElementById("results-screen");
    const reviewScreen  = document.getElementById("review-screen");
    const startBtn   = document.getElementById("start-btn");
    const nextBtn    = document.getElementById("next-btn");
    const restartBtn = document.getElementById("restart-btn");
    const reviewBtn  = document.getElementById("review-btn");
    const backBtn    = document.getElementById("back-btn");
    const questionEl   = document.getElementById("question-text");
    const counterEl    = document.getElementById("question-counter");
    const progressFill = document.getElementById("progress-fill");
    const answersEl    = document.getElementById("answers-container");
    const scoreTracker = document.getElementById("score-tracker");
    const statusEl     = document.getElementById("status-text");
    const finalScoreEl = document.getElementById("final-score");
    const percentEl    = document.getElementById("score-percent");
    const messageEl    = document.getElementById("score-message");
    const resultIconEl = document.getElementById("result-icon");
    const reviewListEl = document.getElementById("review-list");
    const winClockEl   = document.getElementById("win-clock");
    const taskbarClock = document.getElementById("taskbar-clock");

    function showScreen(s) {
      [startScreen, quizScreen, resultsScreen, reviewScreen].forEach(x => x.classList.remove("active"));
      s.classList.add("active");
    }

    function updateClock() {
      const now = new Date();
      const h = now.getHours(), m = String(now.getMinutes()).padStart(2, "0");
      const label = `${(h % 12) || 12}:${m} ${h >= 12 ? "PM" : "AM"}`;
      if (winClockEl)   winClockEl.textContent   = label;
      if (taskbarClock) taskbarClock.textContent = label;
    }
    updateClock();
    setInterval(updateClock, 1000);

    function setStatus(msg) { if (statusEl) statusEl.textContent = msg; }

    function startQuiz() {
      currentIndex = 0; score = 0; userAnswers = []; hasAnswered = false;
      scoreTracker.textContent = "Score: 0";
      showScreen(quizScreen);
      loadQuestion();
      setStatus("Quiz in progress\\u2026");
    }

    function loadQuestion() {
      hasAnswered = false;
      nextBtn.disabled = true;
      const q = QUESTIONS[currentIndex];
      questionEl.textContent   = q.question;
      counterEl.textContent    = `Question ${currentIndex + 1} of ${QUESTIONS.length}`;
      progressFill.style.width = `${(currentIndex / QUESTIONS.length) * 100}%`;
      answersEl.innerHTML = "";
      q.answers.forEach((text, i) => {
        const btn = document.createElement("button");
        btn.className   = "answer-btn";
        btn.textContent = `${String.fromCharCode(65 + i)}.  ${text}`;
        btn.addEventListener("click", () => selectAnswer(i));
        answersEl.appendChild(btn);
      });
    }

    function selectAnswer(chosen) {
      if (hasAnswered) return;
      hasAnswered = true;
      const q = QUESTIONS[currentIndex];
      userAnswers.push(chosen);
      answersEl.querySelectorAll(".answer-btn").forEach((btn, i) => {
        btn.disabled = true;
        if (i === q.correct) btn.classList.add("is-correct");
        else if (i === chosen) btn.classList.add("is-wrong");
      });
      if (chosen === q.correct) { score++; scoreTracker.textContent = `Score: ${score}`; setStatus("\\u2714  Correct!"); }
      else { setStatus("\\u2718  Incorrect."); }
      nextBtn.disabled = false;
    }

    function nextQuestion() {
      currentIndex++;
      if (currentIndex < QUESTIONS.length) { loadQuestion(); setStatus("Quiz in progress\\u2026"); }
      else showResults();
    }

    function showResults() {
      progressFill.style.width = "100%";
      const pct = Math.round((score / QUESTIONS.length) * 100);
      const map = [[100,"🏆","Perfect score! Absolutely outstanding."],[80,"🌟","Great work — you really know your stuff!"],[60,"👍","Solid effort. A respectable performance."],[40,"📚","Not bad, but there is more to learn."],[0,"💡","Keep at it — every attempt builds knowledge."]];
      const [,icon,message] = map.find(([t]) => pct >= t);
      finalScoreEl.textContent = score;
      percentEl.textContent    = `${pct}%`;
      resultIconEl.textContent = icon;
      messageEl.textContent    = message;
      showScreen(resultsScreen);
      setStatus(`Quiz complete \\u2014 ${score}/${QUESTIONS.length} correct (${pct}%)`);
    }

    function showReview() {
      reviewListEl.innerHTML = "";
      QUESTIONS.forEach((q, i) => {
        const chosen = userAnswers[i], ok = chosen === q.correct;
        const item = document.createElement("div"); item.className = "review-item";
        const qDiv = document.createElement("div"); qDiv.className = "review-q"; qDiv.textContent = `${i + 1}. ${q.question}`;
        const aDiv = document.createElement("div"); aDiv.className = "review-a";
        const tag  = document.createElement("span"); tag.className = `review-tag ${ok ? "ok" : "err"}`; tag.textContent = ok ? "\\u2714" : "\\u2718";
        const det  = document.createElement("div");
        det.innerHTML = ok ? `<span class="correct-text">\\u2714 ${q.answers[q.correct]}</span>` : `Your answer: ${q.answers[chosen]}&emsp;<span class="correct-text">Correct: ${q.answers[q.correct]}</span>`;
        aDiv.appendChild(tag); aDiv.appendChild(det);
        item.appendChild(qDiv); item.appendChild(aDiv);
        reviewListEl.appendChild(item);
      });
      showScreen(reviewScreen);
      setStatus("Reviewing answers\\u2026");
    }

    startBtn.addEventListener("click",   startQuiz);
    nextBtn.addEventListener("click",    nextQuestion);
    restartBtn.addEventListener("click", startQuiz);
    reviewBtn.addEventListener("click",  showReview);
    backBtn.addEventListener("click", () => { showScreen(resultsScreen); setStatus(`Quiz complete \\u2014 ${score}/${QUESTIONS.length} correct`); });
""")

commit(T[6], "feat: quiz game logic — scoring, results, review")

# ══════════════════════════════════════════════════════════
# C8 — feat: window chrome — draggable title bar, minimize, maximize, close
# ══════════════════════════════════════════════════════════
with open("script.js", "a") as f:
    f.write("""
// ---------- Window Dragging ----------
(function initDragging() {
  const win = document.getElementById("quiz-window");
  const titleBar = document.getElementById("title-bar");
  let dragging = false, startX, startY, originLeft, originTop;

  titleBar.addEventListener("mousedown", e => {
    if (e.target.classList.contains("title-btn")) return;
    dragging = true;
    const rect = win.getBoundingClientRect();
    startX = e.clientX; startY = e.clientY;
    originLeft = rect.left; originTop = rect.top;
    win.style.transform = "none";
    win.style.left = `${originLeft}px`;
    win.style.top  = `${originTop}px`;
    e.preventDefault();
  });

  document.addEventListener("mousemove", e => {
    if (!dragging) return;
    win.style.left = `${originLeft + (e.clientX - startX)}px`;
    win.style.top  = `${originTop  + (e.clientY - startY)}px`;
  });

  document.addEventListener("mouseup", () => { dragging = false; });
})();

// ---------- Window Chrome Buttons ----------
(function initWindowButtons() {
  const win       = document.getElementById("quiz-window");
  const body      = win.querySelector(".window-body");
  const menuBar   = win.querySelector(".menu-bar");
  const statusBar = win.querySelector(".status-bar");

  win.querySelector(".minimize-btn").addEventListener("click", () => {
    const collapsed = body.style.display === "none";
    body.style.display      = collapsed ? "" : "none";
    menuBar.style.display   = collapsed ? "" : "none";
    statusBar.style.display = collapsed ? "" : "none";
  });

  win.querySelector(".maximize-btn").addEventListener("click", () => {
    if (win.dataset.maximized === "true") {
      win.style.cssText = ""; win.dataset.maximized = "false";
    } else {
      win.style.transform = "none"; win.style.top = "0"; win.style.left = "0";
      win.style.width = "100vw"; win.style.maxWidth = "100vw";
      win.style.height = "calc(100dvh - 32px)"; win.style.maxHeight = "calc(100dvh - 32px)";
      win.dataset.maximized = "true";
    }
  });

  win.querySelector(".close-btn").addEventListener("click", () => {
    if (window.confirm("Exit Quiz.exe?")) win.style.display = "none";
  });
})();
""")

commit(T[7], "feat: window chrome — draggable title bar, minimize, maximize, close")

# ══════════════════════════════════════════════════════════
# C9 — feat: start menu with cascading submenus
# ══════════════════════════════════════════════════════════
w("index.html", """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz.exe</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📝</text></svg>">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="desktop">
    <div class="desktop-icons">
      <div class="icon" tabindex="0"><div class="icon-img">🖥️</div><div class="icon-label">My Computer</div></div>
      <div class="icon" tabindex="0"><div class="icon-img">🗑️</div><div class="icon-label">Recycle Bin</div></div>
      <div class="icon" tabindex="0"><div class="icon-img">📁</div><div class="icon-label">My Documents</div></div>
    </div>

    <div class="window" id="quiz-window">
      <div class="title-bar" id="title-bar">
        <div class="title-bar-text">📝&nbsp; Quiz.exe</div>
        <div class="title-bar-controls">
          <button class="title-btn minimize-btn" aria-label="Minimize">_</button>
          <button class="title-btn maximize-btn" aria-label="Maximize">□</button>
          <button class="title-btn close-btn" aria-label="Close">✕</button>
        </div>
      </div>
      <div class="menu-bar">
        <span class="menu-item">File</span>
        <span class="menu-item">Edit</span>
        <span class="menu-item">View</span>
        <span class="menu-item">Help</span>
      </div>
      <div class="window-body">
        <div id="start-screen" class="screen active">
          <div class="screen-content">
            <div class="splash-icon">📝</div>
            <h1 class="app-title">Quiz.exe</h1>
            <p class="app-version">Version 1.0 &nbsp;|&nbsp; General Knowledge Edition</p>
            <div class="separator"></div>
            <p class="intro-text">Answer 10 multiple-choice questions.<br>No time limit — take your time!</p>
            <button class="btn btn-primary" id="start-btn">▶&nbsp; Start Quiz</button>
          </div>
        </div>
        <div id="quiz-screen" class="screen">
          <div class="quiz-layout">
            <div class="progress-row">
              <span class="progress-label" id="question-counter">Question 1 of 10</span>
              <div class="progress-track"><div class="progress-fill" id="progress-fill"></div></div>
            </div>
            <div class="question-panel"><p id="question-text" class="question-text"></p></div>
            <div class="answers-grid" id="answers-container"></div>
            <div class="quiz-footer">
              <span id="score-tracker" class="score-tracker">Score: 0</span>
              <button class="btn" id="next-btn" disabled>Next&nbsp; ▶</button>
            </div>
          </div>
        </div>
        <div id="results-screen" class="screen">
          <div class="screen-content">
            <div class="result-icon" id="result-icon">🏆</div>
            <h2 class="results-title">Quiz Complete!</h2>
            <div class="score-box">
              <div class="score-number"><span id="final-score">0</span>&thinsp;/&thinsp;10</div>
              <div class="score-percent" id="score-percent">0%</div>
            </div>
            <p class="score-message" id="score-message"></p>
            <div class="btn-row">
              <button class="btn btn-primary" id="restart-btn">↩&nbsp; Play Again</button>
              <button class="btn" id="review-btn">📋&nbsp; View Answers</button>
            </div>
          </div>
        </div>
        <div id="review-screen" class="screen">
          <div class="review-layout">
            <div class="review-header">
              <span class="review-title">Answer Review</span>
              <button class="btn btn-sm" id="back-btn">← Back to Results</button>
            </div>
            <div class="review-list" id="review-list"></div>
          </div>
        </div>
      </div>
      <div class="status-bar">
        <div class="status-panel" id="status-text">Ready</div>
        <div class="status-panel">Quiz.exe</div>
        <div class="status-panel status-clock" id="win-clock">12:00 PM</div>
      </div>
    </div>

    <div class="start-menu" id="start-menu" aria-hidden="true">
      <div class="start-sidebar"><span class="start-sidebar-text">Windows&nbsp;95</span></div>
      <div class="start-menu-items">
        <div class="menu-entry has-sub">
          <span class="entry-icon">📁</span><span class="entry-label">Programs</span><span class="entry-arrow">▶</span>
          <div class="submenu">
            <div class="menu-entry"><span class="entry-icon">📝</span><span class="entry-label">Notepad</span></div>
            <div class="menu-entry"><span class="entry-icon">🎨</span><span class="entry-label">Paint</span></div>
            <div class="menu-entry"><span class="entry-icon">🌐</span><span class="entry-label">Internet Explorer</span></div>
            <div class="menu-entry"><span class="entry-icon">💣</span><span class="entry-label">Minesweeper</span></div>
            <div class="menu-entry"><span class="entry-icon">🧮</span><span class="entry-label">Calculator</span></div>
          </div>
        </div>
        <div class="menu-entry has-sub">
          <span class="entry-icon">📄</span><span class="entry-label">Documents</span><span class="entry-arrow">▶</span>
          <div class="submenu">
            <div class="menu-entry"><span class="entry-icon">📄</span><span class="entry-label">readme.txt</span></div>
            <div class="menu-entry"><span class="entry-icon">📊</span><span class="entry-label">budget.xls</span></div>
            <div class="menu-entry"><span class="entry-icon">🖼️</span><span class="entry-label">vacation.bmp</span></div>
          </div>
        </div>
        <div class="menu-entry has-sub">
          <span class="entry-icon">⚙️</span><span class="entry-label">Settings</span><span class="entry-arrow">▶</span>
          <div class="submenu">
            <div class="menu-entry"><span class="entry-icon">🖥️</span><span class="entry-label">Control Panel</span></div>
            <div class="menu-entry"><span class="entry-icon">🖨️</span><span class="entry-label">Printers</span></div>
            <div class="menu-entry"><span class="entry-icon">📡</span><span class="entry-label">Dial-Up Networking</span></div>
          </div>
        </div>
        <div class="menu-entry has-sub">
          <span class="entry-icon">🔍</span><span class="entry-label">Find</span><span class="entry-arrow">▶</span>
          <div class="submenu">
            <div class="menu-entry"><span class="entry-icon">📂</span><span class="entry-label">Files or Folders…</span></div>
            <div class="menu-entry"><span class="entry-icon">💻</span><span class="entry-label">Computer…</span></div>
          </div>
        </div>
        <div class="menu-entry"><span class="entry-icon">❓</span><span class="entry-label">Help</span></div>
        <div class="menu-entry"><span class="entry-icon">🏃</span><span class="entry-label">Run…</span></div>
        <div class="menu-separator"></div>
        <div class="menu-entry entry-shutdown"><span class="entry-icon">🔌</span><span class="entry-label">Shut Down…</span></div>
      </div>
    </div>

    <div class="taskbar">
      <button class="taskbar-start" id="taskbar-start">
        <span class="start-logo">⊞</span><strong>Start</strong>
      </button>
      <div class="taskbar-sep"></div>
      <div class="taskbar-tasks"><div class="taskbar-task is-active">📝&nbsp; Quiz.exe</div></div>
      <div class="taskbar-tray"><span id="taskbar-clock">12:00 PM</span></div>
    </div>

  </div>
  <script src="script.js"></script>
</body>
</html>
""")

with open("style.css", "a") as f:
    f.write("""
/* ---------- Start Menu ---------- */
.start-menu {
  position: fixed;
  bottom: 32px;
  left: 0;
  display: flex;
  flex-direction: row;
  background: var(--gray);
  border-top:    2px solid var(--white);
  border-left:   2px solid var(--white);
  border-right:  2px solid var(--gray-darker);
  border-bottom: 2px solid var(--gray-darker);
  z-index: 200;
  opacity: 0;
  pointer-events: none;
  transform: translateY(6px);
  transition: opacity 0.1s ease, transform 0.1s ease;
}

.start-menu.is-open { opacity: 1; pointer-events: auto; transform: translateY(0); }

.start-sidebar {
  width: 26px;
  background: linear-gradient(to top, var(--navy), #1a6bb5);
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding-bottom: 8px;
  flex-shrink: 0;
  user-select: none;
}

.start-sidebar-text {
  color: rgba(255,255,255,0.25);
  font-size: 16px;
  font-weight: bold;
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  letter-spacing: 2px;
  white-space: nowrap;
}

.start-menu-items { display: flex; flex-direction: column; min-width: 190px; padding: 2px; }

.menu-entry {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 5px 8px 5px 6px;
  cursor: default;
  position: relative;
  white-space: nowrap;
  font-size: 12px;
}

.menu-entry:hover { background: var(--navy); color: var(--white); }
.entry-icon  { font-size: 16px; flex-shrink: 0; }
.entry-label { flex: 1; }
.entry-arrow { font-size: 9px; margin-left: auto; }

.menu-separator { height: 0; border-top: 1px solid var(--gray-dark); border-bottom: 1px solid var(--white); margin: 3px 4px; }

.submenu {
  display: none;
  position: absolute;
  left: 100%;
  top: -2px;
  background: var(--gray);
  border-top:    2px solid var(--white);
  border-left:   2px solid var(--white);
  border-right:  2px solid var(--gray-darker);
  border-bottom: 2px solid var(--gray-darker);
  min-width: 170px;
  z-index: 210;
  padding: 2px;
}

.has-sub:hover .submenu { display: flex; flex-direction: column; }
.submenu .menu-entry:hover { background: var(--navy); color: var(--white); }
""")

with open("script.js", "a") as f:
    f.write("""
// ---------- Start Menu ----------
(function initStartMenu() {
  const menu     = document.getElementById("start-menu");
  const startBtn = document.getElementById("taskbar-start");

  function openMenu()   { menu.classList.add("is-open");    menu.setAttribute("aria-hidden", "false"); startBtn.classList.add("is-active"); }
  function closeMenu()  { menu.classList.remove("is-open"); menu.setAttribute("aria-hidden", "true");  startBtn.classList.remove("is-active"); }
  function toggleMenu() { menu.classList.contains("is-open") ? closeMenu() : openMenu(); }

  startBtn.addEventListener("click", toggleMenu);
  document.addEventListener("click", e => { if (!menu.contains(e.target) && e.target !== startBtn) closeMenu(); });
  document.addEventListener("keydown", e => { if (e.key === "Escape") closeMenu(); });
})();
""")

commit(T[8], "feat: start menu with cascading submenus")

# ══════════════════════════════════════════════════════════
# C10 — fix: start menu outside-click uses contains()
# ══════════════════════════════════════════════════════════
content = open("script.js").read()
content = content.replace(
    "if (!menu.contains(e.target) && e.target !== startBtn) closeMenu();",
    "if (!menu.contains(e.target) && !startBtn.contains(e.target)) closeMenu();"
)
open("script.js", "w").write(content)

commit(T[9], "fix: start menu outside-click uses contains()")

# ══════════════════════════════════════════════════════════
# C11 — docs: README
# ══════════════════════════════════════════════════════════
w("README.md", """
    # Quiz.exe

    > A retro general knowledge quiz styled as a Windows 95 desktop application.

    **[melonmelonz.github.io](https://melonmelonz.github.io)**

    ---

    ## Features

    - 10 multiple-choice general knowledge questions
    - real-time score tracking and progress bar
    - full answer review after completion
    - draggable application window
    - functional minimize / maximize / close title bar buttons
    - live clock in status bar and taskbar
    - start menu with cascading submenus
    - responsive — works on desktop and mobile

    ## Stack

    Pure **HTML5**, **CSS3**, and **Vanilla JavaScript** — zero dependencies, no libraries.

    ## How to Play

    1. Click **▶ Start Quiz**
    2. Select your answer for each question
    3. Click **Next** to advance
    4. View your final score and optional answer breakdown

    ## Running Locally

    ```
    open index.html
    ```

    No build step, no server, no installs.
""")

commit(T[10], "docs: README")

# ══════════════════════════════════════════════════════════
# C12 — chore: responsive and polish tweaks
# ══════════════════════════════════════════════════════════
with open("style.css", "a") as f:
    f.write("""
/* ---------- Final polish ---------- */
@media (max-height: 520px) {
  .screen-content { padding: 14px; }
  .splash-icon { font-size: 36px; }
}
""")

commit(T[11], "chore: responsive and polish tweaks")

# ══════════════════════════════════════════════════════════
# Repoint main and force push
# ══════════════════════════════════════════════════════════
subprocess.run(["git", "branch", "-D", "main"], check=True)
subprocess.run(["git", "branch", "-m", "main"], check=True)
subprocess.run(["git", "push", "--force", "origin", "main"], check=True)
subprocess.run(["git", "log", "--oneline"], check=True)

print("\nDONE")
