#!/bin/python3
import os
import sys
import shutil

def main():
    #print("Args: {}".format(sys.argv))
    target_dir=sys.argv[1]
    #print("First arg: {}".format(arg))
    #target_dir=os.fspath(arg)
    
    # ID the folder to scan
    if os.path.isdir(os.path.normpath(target_dir)) == False:
        sys.exit("Error: {} is not a directory.  On Windows: Make sure to omit the final '\\'".format(os.path.normpath(target_dir)))
    else:
        print("Scanning {}".format(os.path.normpath(target_dir)))

    # ID the region strings we want to keep
    # World, US, USA, EU, UK
    global target_regions
    #target_regions=['(World)', 'US', '(USA)', 'EU', 'UK', 'En,', '(Europe)']
    target_regions=['(World)', '(Canada)', '(USA)', '(Australia)', ', USA', '(En)', 'En,', '(Europe)', ', Europe']
    
    scan(os.path.normpath(target_dir))

def scan(scan_target):
    # ID the folder to place 'non-region-match' objects into
    # First find the parent of the scan_target
    target_parent=os.path.dirname(os.path.normpath(scan_target))
    #print("Parent ", target_parent)
    # Now find the name of the directory we are scanning
    target_name=os.path.basename(os.path.normpath(scan_target))
    #print("Name ", target_name)

    nonmatch_dir=(os.path.join(target_parent, target_name+"-nonregion"))
    #nonmatch_dir=nonmatch_dir.rstrip('/')
    print("non-matching dir: {}".format(nonmatch_dir))
    if os.path.exists(nonmatch_dir):
        nonmatch_dir_exists = True
    else:
        nonmatch_dir_exists = False

    with os.scandir(scan_target) as collection:
        for object in collection:
            if object.is_file:
                # Get the base name
                object_base=os.path.basename(object)
                # Strip off the extension
                object_name=os.path.splitext(object_base)
                #print("Object name split: {} {}".format(object_name[0], object_name[1]))
                # For each object in the scan target - inspect it's name for a region string
                region_match=False
                
                for region in target_regions:    
                    if region in object_name[0]:
                        region_match=True

                if region_match == True:
                    #print("Region match: {}".format(object))
                    pass
                else:
                    print("Region miss: {}".format(object))
                    if nonmatch_dir_exists == False:
                    #    os.makedirs(nonmatch_dir)
                        nonmatch_dir_exists = True
                    #shutil.move(object, nonmatch_dir)
                    


  
if __name__ == '__main__':
    print("starting script")
    main()