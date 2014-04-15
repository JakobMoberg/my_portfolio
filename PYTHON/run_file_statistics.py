  
#    created by Jakob Moberg, moberg.jakob@gmail.com 15/4/2014
#    Start-function: main part of script, 
#    program for comparing two folders of tab delimited txt files
  

import glob
import os

# folder assumed to have correct data in .txt files
lib="C:/correct"

#folder to be tested
test_lib="c:/test"

check_folder(lib,test_lib)



def check_file(lib_ref,lib_test,fileName):
#Compares two version of a text file with name=fileName in the two difference 
# folders lib_ref and lib_test
 
    f_ref=open(lib_ref+"/"+fileName,'r')
    data_ref=f_ref.read()
    lines_ref=data_ref.split('\n') 
    col_names_ref=lines_ref[0]
    col_list_ref=col_names_ref.split('\t')
    f_ref.close()
    
    f_test=open(lib_test+"/"+fileName,'r')
    data_test=f_test.read()
    f_test.close()
    lines_test=data_test.split('\n')
    col_names_test=lines_test[0]
    col_list_test=col_names_test.split('\t')
    f_test.close()


    print "Testing file:\n" +fileName + "\n"
    
    rows_test=len(lines_test)
    rows_ref=len(lines_ref)
    
 #if differences in number of rows found. print the number of rows   
    if rows_test!=rows_ref:
        print "Rows in test file: " + str(rows_test)
        print "Rows in ref file: " + str(rows_ref)
        
    test_only,ref_only=match_lists(col_list_test, col_list_ref)
    print_missing_item(test_only,ref_only,"Columns","ONLY in test:","NOT in test file:")
    print 100*"-"  
            
   
def match_lists(list1,list2):
    list1_only=[]
    list2_only=[]
    list1_only=list(set(list1)-set(list2))
    list2_only=list(set(list2)-set(list1))    

    return list1_only,list2_only
  
def print_missing_item(list1,list2,header,l1_text,l2_text):
#prints header if the lists have different length
    if len(list1)>0 or len(list2)>0:
        print header

#prints itemss and message for data containted in list1        
    if len(list1)>0:
        print l1_text
        for s in list1:
            print "\t"+s

#prints itemss and message for data containted in list2
    if len(list2)>0:
        print l2_text
        for s in list2:
            print "\t"+s
            
def check_folder(lib_ref,lib_test):
#    Checks the test_lib vs lib for all .txt files and prints diagnostics
    ref_dir=[]
    os.chdir(lib_ref)
    for file in glob.glob("*.txt"):
        ref_dir.append(file)
    
    ref_nf=len(ref_dir)   
    
    lib=test_lib
    test_dir=[]
        
    os.chdir(lib)
    for file in glob.glob("*.txt"):
        test_dir.append(file)
    
    test_nf=len(test_dir)
    
    print 100*"-"
    print "Testing dir: "+ test_lib + " ..."
    print 100*"-"
    print "Overall statistics"
    print 100*"-"
    print "Number of files:"+ str(test_nf)
    print "Files in reference folder: " +str(ref_nf)
    
    print 100*"-"
    test_only,ref_only=match_lists(test_dir,ref_dir)
    print_missing_item(test_only,ref_only,"File status:","In test folder but not in reference folder:","Missing in test folder:")
    print 100*"-"
    
    in_both=list(set(test_dir)&set(ref_dir))
    for item in in_both:
        
#Compares files contained in both of the folders
        check_file(lib_ref,test_lib,item) 
  
 
