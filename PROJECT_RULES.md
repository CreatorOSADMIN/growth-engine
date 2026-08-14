# Project Rules

1. third-party/ contains upstream open-source projects.
2. Never modify third-party projects directly unless explicitly required.
3. Internal functionality belongs inside app/ or engines/.
4. All Claude changes must arrive as .patch files.
5. Never apply a patch without running git apply --check first.
6. Every feature must include tests where practical.
7. Do not automatically publish spam, irrelevant comments, or deceptive content.
8. Respect robots.txt, rate limits, terms of service and applicable laws.
9. Keep API keys and credentials outside Git.
10. Prefer local/open-source infrastructure whenever practical.
