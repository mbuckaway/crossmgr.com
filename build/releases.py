import github
import os
import logging

logger = logging.getLogger(__name__)

github_conn = github.Github("2a559cd9ab84ffc6993aa7cd4b97478e56872926")
try:
    repo = github_conn.get_repo('mbuckaway/CrossMgr', lazy=False)
except github.GithubException:
    raise ReferenceError("Repo not found")

windows_releases = []
linux_releases = []
macosx_releases = []

try:
    working_release = repo.get_latest_release()
    #working_release = repo.get_release(opts["tag"])
    print('Release ID: {}'.format(working_release.id))
    print('Tag: {}'.format(working_release.tag_name))
    print('Title: {}'.format(working_release.title))
    print('URL: {}'.format(working_release.url))
    print('Body: {}'.format(working_release.body))

    for asset in working_release.get_assets():
        extparts = asset.name.split('.')
        ext = extparts[len(extparts)-1].upper()
        if ext == 'APPIMAGE':
            linux_releases.append(asset)
        elif ext == "EXE":
            windows_releases.append(asset)
        elif ext == "DMG":
            macosx_releases.append(asset)

except github.GithubException:
    logger.info("No release found!")
    working_release = None

print("Windows Releases:")
for asset in windows_releases:
    #, asset.browser_download_url
    print("Name: {0} {1:8.1f}kb {2}".format(asset.name, asset.size/1000, asset.created_at))

print("MacOSX Releases:")
for asset in macosx_releases:
    print("Name: {0} {1:8.1f}kb {2}".format(asset.name, asset.size/1000, asset.created_at))

print("Linux Releases:")
for asset in linux_releases:
    print("Name: {0} {1:8.1f}kb {2}".format(asset.name, asset.size/1000, asset.created_at))

