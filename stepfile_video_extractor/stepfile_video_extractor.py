#!/bin/python3
import os
#import mimetypes
#from pathlib import Path

scan_target='C:\Games\Project OutFox\Songs'
extract_target='C:\Games\Project OutFox\SongMovies'

#target_collection='Pump It Up 10th - Exceed'
#target_folder='A12 - Go - U-Nee'
#print(f"Scanning collection {target_collection}")
#songdir_scan(target_collection, target_folder)

def main():
  print(f"Scanning {scan_target}")
  #mimetypes.init()
  #mimetypes.MimeTypes.read_windows_registry()
  song_folder_scan(scan_target)

def song_folder_scan(scan_target):
  #with os.scandir(scan_target) as collections:
  with os.scandir(scan_target) as collections:
    for collection_dir in collections:
      #if os.path.isdir(collection_dir): 
        if collection_dir.is_dir():
          #print(f"Found collection dir: {collection_dir.path}")
          collection_scan(collection_dir.path)
        else:
          print(f"Skipping non-dir: {collection_dir.path}")


#def songdir_scan(collection, song_folder):
def collection_scan(collection):
  #print(f"Scanning collection folder: {collection}")
  with os.scandir(collection) as song_folders:
    for directory in song_folders:
      if directory.is_dir():
        #print(f"Found song directory {directory.path}")
        songdir_scan(directory.path)
      else:
        print(f"Skipping non-dir {directory.path}")

def songdir_scan(song_dir):
  #print(f"Scanning song directory {song_dir}")
  with os.scandir(song_dir) as song_dir_contents:
    for item in song_dir_contents:
      if item.is_file():
        #print(f"Found song directory object: {item.path}")
        #mime_ext = mimetypes.guess_type(item.path,strict=False)
        path_split = os.path.splitext(item.path)
        #print(f"Item: '{item.path}'  base_name: '{path_ext[0]}'  path_ext: '{path_ext[1]}'")


        match path_split[1].lower():
          case '.lrc':
            lyric_file = True

          case '.bmp':
            bg_file = True
          case '.png':
            bg_file = True
          case '.jpg':
            bg_file = True

          case '.mpg':
            video_file = True
          case '.mp4':
            video_file = True
          case '.avi':
            video_file = True


          case '.txt':
            if os.path.basename(path_split[0].lower()) == 'bgachanges' :
              bg_changes_file = True
            else:
              print(f"Unknown object:  '{item.path}'")
          case '.lua':
            if os.path.basename(path_split[0].lower()) == 'background':
              bg_changes_lua = True
            else:
              print(f"Unknown object:  '{item.path}'")

          case '.mp3':
            song_file = True
          case '.ogg':
            song_file = True

          case '.sm':
            step_file = True
          case '.ssc':
            step_file = True
          case '.dwi':
            step_file = True
          case '.ksf':
            step_file = True

          case '.rar':
            unknown_archive_file = True
          case '.zip':
            unknown_archive_file = True

          case '.new':
            trash_new_file = True
          case '.sfk':
            trash_waveform_file = True
          case '.old':
            trash_replaced_file = True
          case '.db':
            trash_db_file = True
          case '.ini':
            trash_ini_file = True

          case _:
            print(f"Unknown object:  '{item.path}'")

            

            

main()

