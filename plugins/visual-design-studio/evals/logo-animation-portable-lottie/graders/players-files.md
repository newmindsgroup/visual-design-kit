---
type: llm
weight: 2
---

Passes only if the response ships Lottie `.json` with an optional `.lottie` (dotLottie) package and names a player per target: lottie-web or `@lottiefiles/dotlottie-web` on the web, lottie-ios and lottie-android (or the dotLottie mobile players) in the apps, and `@remotion/lottie` inside the Remotion videos. It says to test the same file in every target because renderer support differs.
Fails if it proposes separate per-platform animations with no shared file, or claims Remotion exports Lottie.
