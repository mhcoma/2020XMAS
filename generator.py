def donothing():
	return

data_file_name = 'data.txt'
data_file = open(data_file_name, 'r')
data = data_file.read()

layout_file_name = 'layout.txt'
layout_file = open(layout_file_name, 'r')
layout = layout_file.read()

print(data)

begin_tag = "xmAS "
increase_tag = "XMAS "
decrease_tag = "xmas "
print_tag = "XMas "
end_tag = "xMAs "
nothing_tag = "XmaS "
space_tag = "     "

output_list = []

output_list.append(begin_tag)

previous = 0
for c in data:
	current = ord(c)
	if current > previous:
		tag = increase_tag
	else:
		tag = decrease_tag
	for i in range(abs(current - previous)):
		output_list.append(tag)
	previous = current
	output_list.append(print_tag)

output_len = len(output_list)

layout_len = 0
for c in layout:
	if c == '#':
		layout_len += 1

output = '''
#include <stdio.h>
#define %s int main() { char n = 0;
#define %s n++;
#define %s n--;
#define %s putchar(n);
#define %s return 0; }
#define %s ;
'''%(begin_tag, increase_tag, decrease_tag, print_tag, end_tag, nothing_tag)

index = 0
for c in layout:
	if c == ' ':
		output += space_tag
	elif c == '#':
		if index < output_len:
			output += output_list[index]
		elif index < layout_len - 1:
			output += nothing_tag
		else:
			output += end_tag
		index += 1
	elif c == '\n':
		output += '\n'

print(output_len)
print(layout_len)
print(index)

output_file_name = 'output.c'
output_file = open(output_file_name, 'w')
output_file.write(output)
	