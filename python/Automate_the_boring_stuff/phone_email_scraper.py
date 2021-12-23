import re, pyperclip
# TODO: create a regex for phone numbers
phoneRegex = re.compile(r"""
(
((\d\d\d)|(\(\d\d\d\)))?
(\s|-)    # first sepapator
\d\d\d    # first 3 digits
-    #separator
\d\d\d\d    #last 4 digits
)
""", re.VERBOSE)

# TODO: create a regex for email addresses
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+ #name part
@               #@ symbol
[a-zA-Z0-9_.+]+ #domain name part



''', re.VERBOSE)
#TODO: get the text off the clipboard
text= pyperclip.paste()
#TODO: extract the email/phone from this
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoNumber in extractedPhone:
    allPhoneNumbers.append(phoNumber[0])



#TODO: copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)



"""
479-205-4874
678-560-3485
724-900-2986
242-391-3183
604-720-6426
651-807-8065
209-754-9111
641-433-6698
701-528-9851
304-491-9583
863-583-8107
507-948-3980
546-367-3454
321-854-5616
904-896-2920
309-387-1990
605-373-2329
573-454-1209
252-822-2439
586-481-1805
615-716-5379
903-995-3368
205-868-3935
881-376-2173
936-631-8841
307-368-4710
631-957-9402
336-402-2815
511-768-9073
862-579-2515
678-439-5117
949-328-4768
764-582-6489
662-882-4349
323-686-4356
321-641-1192
980-511-2211
931-381-2749
557-314-1719
641-845-9700
571-248-3160
611-848-3013
724-392-9051
303-606-9242
419-691-5429
740-228-1291
479-529-9642
308-702-9334
704-481-3176
270-245-5606
559-639-2831
506-203-1818
716-387-4756
501-919-6026
351-796-1964
809-948-1893
984-578-4176
765-298-6852
309-531-8927
561-405-2390
423-694-1512
561-365-7342
717-616-6054
517-593-3243
971-374-3441
313-758-7914
713-418-9707
811-557-8092
601-247-7920
405-866-8158
940-998-9912
904-383-5407
772-773-7846
312-773-6768
814-960-3437
703-767-4323
403-212-2346
805-997-2016
415-595-9796
252-739-5595
473-406-4822
778-569-3862
410-418-7216
816-614-7357
307-476-5699
939-537-1879
905-523-5311
975-675-8521
515-420-4722
573-286-5790
646-934-6224
473-909-5259
425-691-6076
740-912-1584
361-423-3274
939-725-1384
484-326-9103
207-389-7224
947-684-9146
877-503-6944
601-896-4565
254-945-4889
417-576-2133
627-632-6773
812-983-9748
303-568-6327
402-497-9729
441-769-3433
641-409-6385
514-637-7967
813-213-1319
704-231-9162
229-718-3131
518-483-3634
231-296-9140
706-899-3971
464-525-8598
464-999-6721
760-690-7194
424-442-9011
211-937-9457
234-238-8851
904-838-7421
320-944-8986
881-674-8231
847-833-3195
jmckay67@aol.com
tjordan@msn.com
ccross20@gmail.com
rayfords66@hotmail.com
jgentry@me.com
wcamacho57@icloud.com
qfranks@comcast.net
cygzfjd61@outlook.com
jfox39@live.com
aparker39@sbcglobal.net
mcdanie3354@att.net
uqcwsntti71@att.net
efrancis@optonline.net
austi363@optonline.net
lbarlow22@me.com
sshepherd61@sbcglobal.net
rterry64@outlook.com
eddiem89@yahoo.com
csimpson8@verizon.net
jmanning54@optonline.net
herickson3@me.com
bgraham70@sbcglobal.net
msloan55@verizon.net
jmcintosh@icloud.com
owenm64@yahoo.com
uzkp@yahoo.com
gramsey51@optonline.net
cramsey91@outlook.com
lfinch@gmail.com
masonm44@att.net
oboyer8@icloud.com
tnjdmbnizb@comcast.net
gmccarthy4@msn.com
tzb23@yahoo.com
cmaddox@yahoo.com
talle6@att.net
jhurst88@outlook.com
epickett85@msn.com
dmcintyre@optonline.net
twilkins7@icloud.com
deandres56@outlook.com
lgross@me.com
cmathews23@verizon.net
chernandez16@yahoo.com
sylvesterg@comcast.net
edaniels@comcast.net
mknapp26@outlook.com
thendrix@me.com
ggonzales@hotmail.com
cwilkinson7@comcast.net
hmoore12@yahoo.com
joyc5185@sbcglobal.net
rgriffin45@optonline.net
sburris@comcast.net
nhuff@att.net
lgibson51@comcast.net
nmendez@mac.com
dkane93@msn.com
alvarad24@live.com
mpittman9@gmail.com
fnolan38@verizon.net
qkane60@me.com
mowens88@aol.com
swarner@mac.com
gedwards@aol.com
gduffy35@optonline.net
cwnzm@hotmail.com
lmays@gmail.com
xugizlf81@live.com
swiley19@sbcglobal.net
dvincent@verizon.net
emorton5@hotmail.com
trentonr64@comcast.net
alonzon17@aol.com
scallahan89@optonline.net
mmorin73@mac.com
vasque3298@comcast.net
jerrodh62@comcast.net
sblanchard44@att.net
renaldon@comcast.net
rlogan97@optonline.net
ysbmcsipr3@comcast.net
dchambers18@sbcglobal.net
mdixon95@me.com
rwright@att.net
mcbrid17@gmail.com
cohe1696@yahoo.com
hwalton3@hotmail.com
jacquesd@att.net
ncleveland88@mac.com
hreeves56@mac.com
dcastro91@mac.com
picket8286@gmail.com
ebryant28@hotmail.com
ltrevino@live.com
lbooker16@me.com
ramse3653@verizon.net
donnym24@live.com
aharmon99@sbcglobal.net
cblanchard@msn.com
zglover61@yahoo.com
rbooth23@mac.com
curtism@verizon.net
ddavid37@sbcglobal.net
qxu@msn.com
crios28@yahoo.com
awilliam86@sbcglobal.net
blanchar7913@icloud.com
jstephenson53@live.com
aubreyk90@msn.com
abels@verizon.net
pmorp6@msn.com
royalw65@verizon.net
hbarber66@sbcglobal.net
cgregory@mac.com
wyat97@gmail.com
maso5913@gmail.com
fsosa33@sbcglobal.net
mccart6795@me.com
gentr9578@verizon.net
wbullock50@hotmail.com
dblake74@sbcglobal.net
wcastaneda@sbcglobal.net
wyates@att.net
hexxuxu97@icloud.com
mcombs2@icloud.com

"""
