# Routes that need little or no tapping

## Files from the Mac to the iPhone

1. Copy the file to the root of iCloud Drive:
   `cp file.png ~/Library/Mobile\ Documents/com~apple~CloudDocs/`
   The root is the first place that the Files app shows, so you tap less.
2. On the iPhone, open Files / Arquivos > iCloud Drive.
3. If the file is not in the list, refresh it. Pull to refresh is a drag, so it works only in full-screen mode. In background mode, go back one level and open iCloud Drive again (not tested yet).
4. Tap the file once. The first tap downloads it. Tap again to open it.
5. For an image, open the Share sheet and tap Save Image / Salvar Imagem. The first time, the phone asks for Photos access. That prompt is the user's. Do not tap a person or a device in the sheet.

## Signed shortcut

Use this when the mirroring window cannot do the job, for example to set a wallpaper. The phone runs the shortcut, so the steps do not depend on taps or gestures.

1. Make the shortcut on the Mac. Two ways:
   - Build it in the Shortcuts / Atalhos app and use File > Export. The exported file is signed.
   - Write the workflow plist yourself, then sign it:
     `shortcuts sign --mode anyone --input unsigned.shortcut --output espelho.shortcut`
2. Copy the signed file to the root of iCloud Drive (see the section above).
3. On the iPhone: Files > iCloud Drive, tap the file, tap Add Shortcut / Adicionar Atalho.
4. Run it from the Shortcuts app with one tap. The first run can ask for permissions. Those are the user's.

For a wallpaper: put the image in iCloud Drive, and make a shortcut with Get File (that image) followed by Set Wallpaper / Definir Papel de Parede. Turn off Show Preview so the shortcut does not wait for a tap.

If iCloud sync for Shortcuts is on, a shortcut made in the Mac app can appear on the phone without a file (not tested yet). Check the Shortcuts app on the phone before you export.

## Apple Configurator

Apple Configurator can set the wallpaper and the Home Screen layout only on a supervised device. Supervising an iPhone erases it. Say this to the user before you suggest it, and do not use it unless the user accepts that the phone is erased.
