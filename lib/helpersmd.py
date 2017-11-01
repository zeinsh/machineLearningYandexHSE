def write_to_file(report,filename):
    f=open("output/"+filename,"w")
    f.write(str(report))
    f.close()
