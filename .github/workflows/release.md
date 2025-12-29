# Release Checklist

## Pre-Release Steps

1. ✅ Update `VERSION` file with new version number
2. ✅ Update `CHANGELOG.md` with all changes since last release
3. ✅ Update version in all README files (README.md, README.de.md, README.tr.md)
4. ✅ **For Major releases (Breaking Changes)**: Review and update `docs/ak-design-system.mcp.md` if architectural changes affect MCP rules or structure
5. ✅ Run build script: `./build.sh`
6. ✅ Test the build output
7. ✅ Commit all changes
8. ✅ Create git tag: `git tag -a v1.2.0 -m "Release v1.2.0"`
9. ✅ Push commits and tags: `git push && git push --tags`

## Version Numbering

- **Major** (x.0.0): Breaking changes
- **Minor** (x.y.0): New features, backwards compatible
- **Patch** (x.y.z): Bug fixes, backwards compatible

## Current Version

See `VERSION` file for current version number.

