# mirroir-mcp

[mirroir-mcp](https://github.com/jfarcand/mirroir-mcp) is a server that drives iPhone Mirroring. It sends taps, typing and scrolling to the mirror window without bringing it to the front. Use it first when it is connected.

## Setup

The install and the macOS permissions are the user's decision. Ask before you install.

1. Install: `npm install -g mirroir-mcp`. It downloads a prebuilt binary and checks its SHA-256. Register `mirroir-mcp-native`, which sits next to the `mirroir-mcp` command, as a stdio MCP server in your client. That path needs no Node at start-up.
   - `npx -y mirroir-mcp install` also works, but it also installs the project's own skill, which repeats this one.
   - The Homebrew formula builds from source. It needs the full Xcode app, and Homebrew asks the user to trust the tap first.
2. Check: `npx -y mirroir-mcp doctor`. It names what is left to fix.
3. The user grants Screen Recording and Accessibility in System Settings. Never change these settings for the user.
4. The server is read-only until `~/.mirroir-mcp/permissions.json` allows more. Propose a short list, and let the user approve it:

```json
{
  "allow": ["describe_screen", "screenshot", "tap", "type_text", "press_key", "swipe", "scroll_to", "launch_app", "press_home", "press_app_switcher", "spotlight"],
  "blockedApps": ["Wallet", "Passwords"]
}
```

Do not propose `"allow": ["*"]`. Add the user's bank and payment apps to `blockedApps`.

## Which tool keeps the user's screen

| Tools | Front app | Use |
|---|---|---|
| `describe_screen`, `screenshot` | Kept | Read the screen. `describe_screen` costs fewer tokens than an image. |
| `tap`, `double_tap`, `long_press` | Kept | Taps land even when other windows cover the mirror. |
| `type_text`, `press_key` | Kept | Typing works in the background. |
| `swipe`, `scroll_to` | Kept | Lists and the Share sheet scroll. |
| `launch_app`, `spotlight`, `press_home`, `press_app_switcher` | Kept | Faster than tapping through the Home Screen. |
| `drag`, `pinch`, `rotate` | Borrowed for about 1 s | Moves icons and widgets. Agree on a time first. |
| `hold_keys`, `touch` | Taken | Avoid while the user works. |

## What it does not change

- The iOS dead ends stay, for example "Unable to Load Photos" in Settings > Wallpaper. Use the routes in `routes.md`.
- The safety lines stay. Passcodes, privacy prompts and people in the Share sheet are the user's.
- Closing iPhone Mirroring stops all input. Tell the user this if they want to stop you.
