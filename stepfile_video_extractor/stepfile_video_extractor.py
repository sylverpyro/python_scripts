import os

scan_target='C:\Games\Project OutFox\Songs'
extract_target='C:\Games\Project OutFox\SongMovies'

def main():
    print(f"Scanning {scan_target}")
    collection_scan()

def collection_scan():
    #with os.scandir(scan_target) as collections:
    with os.scandir(scan_target) as collections:
        for collection_dir in collections:
            #if os.path.isdir(collection_dir): 
            if collection_dir.is_dir():
                print(f"Found collection dir: {collection_dir.path}")
            else:
                print(f"Skipping non-dir: {collection_dir.path}")


    #target_collection='Pump It Up 10th - Exceed'
    #target_folder='A12 - Go - U-Nee'
    #print(f"Scanning collection {target_collection}")
    #songdir_scan(target_collection, target_folder)

def songdir_scan(collection, song_folder):
    full_path=scan_target + collection + song_folder
    print(f"Scanning song folder: {full_path}")

main()

