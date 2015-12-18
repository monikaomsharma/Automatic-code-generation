#!usr/bin/env/python

name = raw_input("Name the file : ")
file_name = name + ".txt"

file_obj = open(file_name,"w")

parameter_no = raw_input("Enter the no of parameters you want: ")
var_parameter = [""]*int(parameter_no)


##############################################################
######### no of parameters required by the user###############
##############################################################
for i in range(0,int(parameter_no)):
        var_parameter[i] = raw_input("Enter value of parameter" + str(i) + "=")

### no of input by the user ###

input_no = raw_input("Enter the no of inputs : ")
var_input = [""]*int(input_no)

for i in range(0,int(input_no)):
	var_input[i] = raw_input("Enter the first input: " + str(i) + "=" )



### no of output by the user ###

parameter_output = raw_input("enter the no of outputs required : ")

output_para = [""]*int(parameter_output)

for i in range(0,int(parameter_output)):
        output_para[i] = raw_input("Enter the firstoutput variable : " + str(i) + "=")

lib = "import numpy\nfrom gnuradio import gr\n"
class_var = "class file_name(gr.sync_block):\n\t"

var_parameter = ",".join(map(str,var_parameter))

def_init = "def __init__(self,"+var_parameter+"):\n\t\t"
var_init = "self.in = []\n\t\ta=[]\n\t\tb = []\n\t\t"
var_loop = "for i in range(0,"+str(input_no)+"):\n\t\t\ta.append(numpy.float32)\n\t\tfor i in range(0,"+str(parameter_output)+"):\n\t\t\tb.append(numpy.float32)\n\t\t"
gr_block = "gr.sync_block.__init__(self,\n\t\t"
gr_name = 'name = "multiply_py_ff",\n\t\t'
gr_in = "in_sig=a,\n\t\t"
gr_out = "out_sig = b\n\n\t"

work = "def work(self,input_items,output_items):\n\t\t"

#work_code = lib + class_var + def_para + def_init + var_init + var_loop + gr_block + gr_name + gr_in + gr_out + work


temp = []
for(i,j) in zip(range(0,int(input_no)),var_input):
        temp.append(j+"=input_items["+str(i)+"]\n\t\t")

list_var = " ".join(map(str,temp))

#logic = raw_input("enter the logic: ")
temp =[]

for(i,j) in zip(range(0,int(parameter_output)),output_para):
        temp.append(j+"=output_items["+str(i)+"]\n\t\t")

list_out = " ".join(map(str,temp))
exp = raw_input("Enter Expression to execute: ")

exp = exp+"\n\t\t"

ret = "return len(output_items[0])"

py_code = lib + class_var + def_init + var_init + var_loop +  gr_block + gr_name + gr_in + gr_out + work + list_var + list_out +exp+ ret

file_obj.write( py_code)

file_obj.close()


fname = name + ".xml"
fobj = open(fname, "w")

cat = raw_input("enter the category you want: ")

blocks = '<?xml version="1.0"?>\n'
add = "<block>\n<name>"+name+"</name>\n<key>"+cat+"</key>\n<category>"+cat+"</category>\n<import>import gnuradio</import>\n"
attach = ["$" + var_parameter for var_parameter in var_parameter]
in_attach = "<make>gnuradio."+fname+"("+str(attach)+")</make>\n"


for i in var_parameter:
	para_no = "<param>\n<name>"+i+"</name>\n<key>"+i+"</key>\n<type></type>\n</param>\n\n"

for i in var_input:
	in_no = "<sink>\n<name>"+i+"</name>\n<type>float</type>\n</sink>\n"

for i in output_para:

	in_source = "<source>\n<name>"+i+"</name>\n<type></type>\n</source>\n</block>\n"

py1_code = blocks + add + in_attach + para_no + in_no + in_source


fobj.write( py1_code)

fobj.close()

