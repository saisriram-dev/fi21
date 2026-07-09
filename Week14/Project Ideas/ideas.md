### Systems & Infrastructure

- **A database engine, not a wrapper around one.** B-tree or LSM storage, a write-ahead log, MVCC for concurrent access, a basic query planner. The hard part isn't storing data — it's surviving a kill -9 mid-write without corrupting itself.
- **A container runtime from scratch.** Skip Docker's API — use Linux namespaces, cgroups, and chroot directly to isolate a process. You'll actually learn what "container" means instead of what docker-compose hides from you.

### AI

- **Pretrain a tiny language model yourself.** Architecture, tokenizer, training loop, all of it — on something narrow and weird, like your group chat history or one author's complete works. It'll be bad at everything except its niche, and that's exactly the point.
- **Actually build Jarvis.** Not a chatbot — an agent that watches your screen, decides what to click, and recovers when it's wrong. The demo is the easy 5%; reliability is the entire project. This is a genuinely unsolved problem right now, not a solved one you're redoing.

### Security

- **Find a real CVE.** Write your own fuzzer, point it at an open-source library you actually use, responsibly disclose whatever turns up. A CVE with your name on it is externally-verified difficulty — stronger than almost anything else on this list.
- **Run a honeypot for a month, then publish the writeup.** Fake vulnerable services, full logging, and a real analysis of what hit them. Security work plus the clear technical writing FAANG loops reward.

### Distributed Systems

- **Implement Raft from the paper, build a key-value store on top of it, then kill nodes mid-write on purpose and document exactly what happens.** The postmortem matters more than the code.
- **A CRDT-based collaborative editor.** Offline edits, conflict resolution, eventual consistency, no central lock. This is the real problem behind Google Docs and Figma multiplayer, not a toy version of it.

### Hardware & Embodied Systems

- **SLAM navigation on cheap hardware.** Raspberry Pi, a camera, a few sensors, a robot that maps and navigates your house without eating the furniture. Simulations behave; the real world doesn't, and that gap is the whole lesson.
- **A full-stack IoT device for a problem you actually have.** Custom PCB, firmware, cloud sync, an app. Going from electrons to UI in one project is rare — and rare is memorable in a stack of resumes.

### Pure Craft

- **A raytracer built from raw math.** No game engine — just linear algebra and light transport equations, rendering something genuinely beautiful. Hard fundamentals with a gorgeous payoff.
- **Reverse-engineer something dead.** An abandoned file format, an old game's save system, discontinued software — rebuilt open source. Equal parts detective work and engineering, and it makes a great interview story.
