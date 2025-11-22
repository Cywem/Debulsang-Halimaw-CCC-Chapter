# Large Files

This directory contains large files that are now **available in the Git repository** using Git LFS (Large File Storage).

## Files in Repository (via Git LFS)

✅ `systemWalkthrough.mp4` (233 MB) - Video walkthrough of the system  
✅ `Manuscript.pdf` (2.6 MB) - Project documentation (located in project root)

These files are stored using **Git LFS** and will be automatically downloaded when you clone the repository.

## About Git LFS

Git LFS (Large File Storage) is a Git extension that replaces large files with text pointers inside Git, while storing the file contents on a remote server. This allows you to:

- Version large files efficiently
- Keep repository clone times fast
- Store files larger than GitHub's 100MB limit (up to 2GB per file)

## Cloning the Repository

When you clone this repository, Git LFS files will be downloaded automatically:

```bash
git clone https://github.com/Cywem/Debulsang-Halimaw-CCC-Chapter.git
```

If you need to manually fetch LFS files:

```bash
git lfs pull
```

## Git LFS Setup (for contributors)

If you want to contribute and work with LFS files:

1. Install Git LFS: `brew install git-lfs` (macOS) or download from https://git-lfs.github.com/
2. Initialize: `git lfs install`
3. Files are already tracked in `.gitattributes`

## Tracked File Types

The following file types are tracked by Git LFS:
- `*.mp4` - Video files
- `*.pdf` - PDF documents

See `.gitattributes` in the repository root for the complete configuration.
