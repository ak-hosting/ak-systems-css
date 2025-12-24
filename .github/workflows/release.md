# Release Checklist

## Pre-Release Steps

1. ✅ Update `VERSION` file with new version number
2. ✅ Update `CHANGELOG.md` with all changes since last release
3. ✅ Update version in all README files (README.md, README.de.md, README.tr.md)
4. ✅ Run build script: `./build.sh`
5. ✅ Test the build output
6. ✅ Commit all changes
7. ✅ Create git tag: `git tag -a v1.2.0 -m "Release v1.2.0"`
8. ✅ Push commits and tags: `git push && git push --tags`

## Version Numbering

- **Major** (x.0.0): Breaking changes
- **Minor** (x.y.0): New features, backwards compatible
- **Patch** (x.y.z): Bug fixes, backwards compatible

## Current Version

See `VERSION` file for current version number.

