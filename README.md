# M3U8 Playlist Collection

A lightweight index of public playlist sources, organized as individual M3U8 pointer files by category and country.

> **Important:** These files are source pointers, not mirrored channel or movie streams. Each file contains one entry linking to an upstream playlist. Nested-playlist support differs between players; if a player does not open a pointer, add the upstream URL directly. This repository does not host video, audio, channel streams, or movie files.

## Contents

- `playlists/all-channels.m3u8` — upstream all-channel index
- `playlists/categories/` — entertainment, movies, news, sports, documentary, music
- `playlists/countries/` — US, UK, Canada, Australia, Vietnam

## Sources

The public channel index references **iptv-org/iptv**:
- Repository: https://github.com/iptv-org/iptv
- Playlist index: https://iptv-org.github.io/iptv/
- Upstream project documentation and contribution/licensing terms: https://github.com/iptv-org/iptv

The original reference repository that inspired this organization is:
- https://github.com/m3u8-xtream/m3u8-xtream-playlist

This collection intentionally excludes third-party movie/TV-on-demand playlist URLs where redistribution or streaming rights are not clear. Public accessibility alone does not establish permission to redistribute content.

## Use

1. Open a playlist file in this repository.
2. Copy its upstream URL from the `#EXTINF` entry if your player cannot resolve nested playlists.
3. Add that URL to a compatible player, subject to the upstream provider's terms and your local law.

## Validate

Run the local format check:

```bash
python scripts/validate_playlists.py
```

The validator checks local M3U structure and HTTP(S) URL syntax. It does not download streams, verify copyright ownership, or guarantee that an upstream playlist is online.

## Scope and rights

- No media files or stream segments are copied into this repository.
- Upstream sources retain their own terms, rights, and availability.
- This repository's documentation and validation script are provided under the MIT License.
- Users are responsible for checking local laws and the rights/terms of each upstream source.
