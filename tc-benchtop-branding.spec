#
# spec file for package tc-benchtop-branding
# Technicomp Benchtop Linux - branding: the Technicomp logos and wallpaper.
#
# Built directly from git (OBS scmsync). As in tc-benchtop-settings, the
# installed files are laid out in this repository as a filesystem tree (usr/)
# that mirrors their final paths, and the spec installs that tree verbatim.
# tools/make-logos generates usr/share/pixmaps/distribution-logos/ from
# source/TECHNICOMP-LABS-LOGO.svg, and tools/make-wallpaper the backgrounds in
# usr/share/backgrounds/tc-benchtop/ from source/TECHNICOMP-LABS-LOGO.png; see
# README.md.
#
Name:           tc-benchtop-branding
Version:        0.1.0
Release:        0
Summary:        Technicomp Benchtop Linux branding
License:        CC-BY-SA-4.0 AND MIT
URL:            https://github.com/TechnicompLabs/benchtop-branding
Source0:        LICENSE
Source1:        COPYING.artwork
BuildArch:      noarch
Requires:       distribution-logos-tc-benchtop = %{version}

%description
Branding of Technicomp Benchtop Linux: the default GNOME desktop background,
with one image for the light style and one for the dark style, and an
alternative background, all offered under Settings, Appearance. The Technicomp
logos are in distribution-logos-tc-benchtop.

%package -n distribution-logos-tc-benchtop
Summary:        Technicomp logos for Technicomp Benchtop Linux
License:        CC-BY-SA-4.0
# In place of openSUSE's logos (distribution-logos-openSUSE-Tumbleweed), with
# the same file names, so that openSUSE's own references show Technicomp's.
Provides:       distribution-logos
Conflicts:      distribution-logos

%description -n distribution-logos-tc-benchtop
The Technicomp logos, at the paths of openSUSE's distribution logos. openSUSE's
packages refer to them: the BGRT boot splash draws light-inline.png at the
bottom of the screen, the GDM login screen shows light-inline.svg, the
distributor-logo icons link to the square logos, and Cockpit uses the icons.

%prep
cp %{SOURCE0} %{SOURCE1} .

%build
# nothing to build

%install
# The files are a filesystem tree (usr/) that mirrors their install paths.
# Under OBS scmsync the repository tree is exposed in the RPM source directory;
# copy it verbatim. The base is auto-detected, as in tc-benchtop-settings, so
# the build does not depend on the exact source layout of the scm bridge.
treeroot=
for base in "%{_sourcedir}" "%{_sourcedir}/%{name}-%{version}" "%{_topdir}/SOURCES" "%{_builddir}/%{name}-%{version}" "%{_builddir}" "$PWD"; do
    if [ -d "$base/usr/share/pixmaps/distribution-logos" ]; then
        treeroot="$base"
        break
    fi
done
if [ -z "$treeroot" ]; then
    echo "ERROR: file tree (usr/) not found under the build sources" >&2
    exit 1
fi
install -d "%{buildroot}"
( cd "$treeroot" && cp -a --no-preserve=ownership usr "%{buildroot}/" )

%files
%license LICENSE COPYING.artwork
# wallpapers
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/tc-benchtop
# their entries in Settings, Appearance
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/tc-benchtop.xml
# the default background
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/schemas
%{_datadir}/glib-2.0/schemas/90-tc-benchtop-branding.gschema.override

%files -n distribution-logos-tc-benchtop
%license COPYING.artwork
%{_datadir}/pixmaps/distribution-logos

%changelog
