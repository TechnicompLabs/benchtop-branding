# tc-benchtop-branding

Branding RPMs for **Technicomp Benchtop Linux** (an immutable Tumbleweed-based openSUSE derivative, built against openSUSE:Factory). Built on OBS directly from this repository via scmsync, as `tc-benchtop-branding` in `home:technicomp:benchtop`.

As in `benchtop-settings`, the installed files are laid out as a filesystem tree that mirrors their final paths, and the spec installs the tree verbatim. Two packages come out of it:

- **tc-benchtop-branding** - the desktop backgrounds in `usr/share/backgrounds/tc-benchtop/`, in the colors of technicomplabs.io: `tc-benchtop-l.png` for the light style (the site's page), `tc-benchtop-d.png` for the dark style (the site's page in dark mode), and `tc-benchtop-board.png`, an alternative in the style of the site's navy board panel. `usr/share/gnome-background-properties/` lists them in Settings, Appearance, and `usr/share/glib-2.0/schemas/90-tc-benchtop-branding.gschema.override` makes the first pair the default. The override sorts after openSUSE's `20_openSUSE-branding.gschema.override`, and glib-compile-schemas lets a later file replace an earlier file's value.
- **distribution-logos-tc-benchtop** - the Technicomp logos in `usr/share/pixmaps/distribution-logos/`. It provides `distribution-logos` in place of `distribution-logos-openSUSE-Tumbleweed`, with the same file names, because openSUSE's own packages refer to those files:
  - `light-inline.png` - the boot screen. openSUSE's Plymouth branding selects the BGRT theme, which openSUSE patched to draw this file at the bottom of the screen (`WatermarkPath`), below the PC maker's firmware logo.
  - `light-inline.svg` - the login screen. gio-branding-openSUSE sets GDM's logo to `/usr/share/gdm/greeter/images/distributor.svg`, and gdm-branding-openSUSE links that to this file. GNOME 50 draws it at its own size, 343 x 64.
  - `square-hicolor.svg`, `square-symbolic.svg` - the `distributor-logo` and `distributor-logo-symbolic` icons (links from distribution-logos-openSUSE-icons).
  - `apple-touch-icon.svg`, `apple-touch-icon.png`, `favicon.ico` - Cockpit's branding.
  - `light-dual-branding.svg` - the full logo, light, for dark backgrounds.

Only the build descriptions (`*.spec`, `*.rpmlintrc`, `README.md`, `.obs/`), the license files, `source/` and `tools/` live outside the tree.

## The logos

`source/TECHNICOMP-LABS-LOGO.svg` is the master: one path, the brain-and-globe mark above the TECHNICOMP LABS wordmark. `tools/make-logos` generates every file in `usr/share/pixmaps/distribution-logos/` from it. It splits the path into the mark (the topmost group of shapes) and the wordmark (everything below), and places them with SVG transforms, leaving the path data itself unchanged. The inline logo is the mark followed by the wordmark, in the light blue of the website's light mark (`#D6E6F5`); the square logos are the mark alone, in the logo's blue.

After changing the source, regenerate and commit the results (run from the repository root; needs rsvg-convert and ImageMagick, for example `brew install librsvg imagemagick`):

```
tools/make-logos
```

The source path is made of straight segments, so the logo is visibly faceted when drawn very large. That does not show at the sizes generated here (64 px and below for the light logos, 128 px for the icons).

## The backgrounds

`tools/make-wallpaper` generates the three backgrounds, 3840 x 2160, from `source/TECHNICOMP-LABS-LOGO.png` (the SVG's straight segments would show at this size). The colors and the board's glow and triangle lattice are taken from the site's stylesheet (`assets/css/main.css`); the script lists each one. After changing the logo or the colors, regenerate and commit the results (run from the repository root; needs Pillow and NumPy, for example `pip3 install pillow numpy`):

```
tools/make-wallpaper
```

The login screen reads its logo when it starts. The boot splash is copied into the initrd, so a changed `light-inline.png` appears on the boot screen only after the next initrd rebuild (for example with a kernel update), as with openSUSE's own logos.

## License

The artwork is CC-BY-SA-4.0 (`COPYING.artwork`); the spec, the tools and the configuration files are MIT (`LICENSE`).

Technicomp, Technicomp Labs, the Technicomp Labs logo and its brain-and-globe mark are trademarks of Technicomp Labs. The CC-BY-SA-4.0 license covers copyright only and grants no rights in these trademarks.
