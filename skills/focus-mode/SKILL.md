---
name: focus-mode
description: Disable autocomplete and AI assistants for distraction-free coding practice. Toggle on before interviews, off after.
---

# Focus Mode

Disable autocomplete and AI coding assistants for authentic interview practice.

## Arguments

- **on**: Enable focus mode (disable autocomplete/AI)
- **off**: Disable focus mode (restore settings)
- **status**: Check current state

## Commands

### Enable Focus Mode

`/focus-mode on`

1. **Save current settings** to `.interview/.focus-backup.json`:
   ```bash
   cp .vscode/settings.json .interview/.focus-backup.json 2>/dev/null || echo "{}" > .interview/.focus-backup.json
   ```

2. **Disable autocomplete** - Update `.vscode/settings.json`:
   ```json
   {
     "editor.quickSuggestions": false,
     "editor.suggestOnTriggerCharacters": false,
     "editor.parameterHints.enabled": false,
     "editor.wordBasedSuggestions": "off",
     "editor.inlineSuggest.enabled": false,
     "editor.acceptSuggestionOnCommitCharacter": false
   }
   ```

3. **List AI extensions to disable**:
   ```bash
   code --list-extensions | grep -iE "copilot|codeium|tabnine|codewhisperer|continue|supermaven|cursor"
   ```

4. **Output instructions**:
   ```
   Focus Mode: ON

   Autocomplete disabled in VS Code settings.

   Please manually disable these AI extensions:
   - [list detected extensions]

   To disable: Cmd+Shift+P → "Extensions: Disable" → select extension

   Run `/focus-mode off` when done to restore settings.
   ```

5. **Create marker file**: `.interview/.focus-mode-active`

### Disable Focus Mode

`/focus-mode off`

1. **Check if focus mode is active**:
   ```bash
   test -f .interview/.focus-mode-active
   ```
   If not active: "Focus mode is not currently active."

2. **Restore settings**:
   ```bash
   cp .interview/.focus-backup.json .vscode/settings.json
   ```

3. **Remove marker**: `rm .interview/.focus-mode-active`

4. **Output**:
   ```
   Focus Mode: OFF

   Settings restored from backup.

   Remember to re-enable your AI extensions:
   Cmd+Shift+P → "Extensions: Enable" → select extensions
   ```

### Check Status

`/focus-mode status`

1. Check for marker file
2. Output:
   ```
   Focus Mode: [ON/OFF]

   [If ON]:
   - Autocomplete: Disabled
   - AI Extensions: Manual check required

   [If OFF]:
   - Settings: Normal
   ```

## Integration

The `/interview` skill checks focus mode status:
- If interview mode required and focus mode OFF → suggest enabling
- Remind user at end of session to run `/focus-mode off`
