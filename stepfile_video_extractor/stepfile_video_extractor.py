#!/bin/python3
import os

scan_target='C:\Games\Project OutFox\Songs'
extract_target='C:\Games\Project OutFox\SongMovies'

#target_collection='Pump It Up 10th - Exceed'
#target_folder='A12 - Go - U-Nee'
#print(f"Scanning collection {target_collection}")
#songdir_scan(target_collection, target_folder)

def main():
    print(f"Scanning {scan_target}")
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
    #full_path=scan_target + collection + song_folder
    print(f"Scanning collection folder: {collection}")
    with os.scandir(collection) as song_folders:
        for directory in song_folders:
            if directory.is_dir():
                #print(f"Found song directory {directory.path}")
                songdir_scan(directory.path)
            else:
                print(f"Skipping non-dir {directory.path}")

def songdir_scan(song_dir):
    print(f"Scanning song directory {song_dir}")
    with os.scandir(song_dir) as song_dir_contents:
        for item in song_dir_contents:
            if item.is_file():
                print(f"Found song directory object: {item.path}")
            

main()

