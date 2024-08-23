import assembler_lib as aslib

line2 = "LOOP: MOV #0x3 R4"
labels = aslib.find_labels_and_orgs([line2])
print(aslib.get_label(line2))
print(labels)
print(aslib.tokenize(line2, labels, 2))