# Release Checklist (v2.0+)

## Pre-Release Steps

1. ✅ **Update Version**:
   - Update `VERSION` file with new version number (SemVer).
   - Update version references in `README.md` (CDN links).

2. ✅ **Update Changelog**:
   - Update `CHANGELOG.md` with all changes since last release.
   - Categorize changes: Added, Changed, Deprecated, Removed, Fixed.

3. ✅ **Documentation**:
   - Update `docs/ak-design-system.mcp.md` if architectural changes affect MCP rules.
   - **For Major Releases**: Ensure `docs/MIGRATION_V2.md` (or newer) is up to date.

4. ✅ **Build & Verify**:
   - Run the new build script: `./build-css.sh`
   - This will:
     - Compile SCSS utilities (`src/scss`)
     - Bundle all CSS files
     - Minify output to `dist/ak-design-system.min.css`
   - Verify `dist/` output manually (check file size and content).
   - Test locally using `demo/index.html`.

5. ✅ **Commit & Tag**:
   - Commit all changes: `git commit -am "chore: release vX.Y.Z"`
   - Create git tag: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`

6. ✅ **Push**:
   - Push commits and tags: `git push origin main --tags`
   - Verify that the new version is available via jsDelivr CDN (takes a few minutes).

## Version Numbering

- **Major** (x.0.0): Breaking changes (e.g. removing utility classes, changing variable names).
- **Minor** (x.y.0): New features, backwards compatible (e.g. new components, new utility variants).
- **Patch** (x.y.z): Bug fixes, backwards compatible (e.g. fix typo, adjust color value).

## Current Version

See `VERSION` file for current version number.
