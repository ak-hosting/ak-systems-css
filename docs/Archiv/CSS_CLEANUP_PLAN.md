# CSS Cleanup Plan (Phase 4)

## Goal
Prepare safe removal of legacy CSS files without breaking consumers.

## Canonical Entry
css/ak-design-system/index.css

## Files Marked for Future Removal
- css/ak-design-system.css
- css/ak-accessibility.css
- css/ak-layout-helpers.css
- css/ak-utilities-bg.css
- css/ak-utilities-border.css
- css/ak-utilities-position.css
- css/ak-utilities-shadow.css
- css/ak-utilities-size.css

## Preconditions for Deletion
- No imports or links reference legacy files
- All consumers use index.css
- One full release cycle completed

## Deletion Strategy
1. Verify zero runtime usage
2. Remove legacy files in one commit
3. Tag release as breaking change (major version)

## Rollback Strategy
- Restore deleted files from previous tag
- Re-point consumers if needed
