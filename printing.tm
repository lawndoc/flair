0: LD 5,0(0)	# set r5 to bottom of dmem
1: LDA 6,-7,5	# set r6 to end of printing's AR
2: SUB 4,5,6	# update current offset
3: LD 2,1(0)	# load arg1 into r2
4: ST 2,-8(5)	# load arg1 into AR
5: LDA 6,-1(6)	# decrement end of stack pointer
6: SUB 4,5,6	# update current offset
7: LD 2,2(0)	# load arg2 into r2
8: ST 2,-9(5)	# load arg2 into AR
9: LDA 6,-1(6)	# decrement end of stack pointer
10: SUB 4,5,6	# update current offset
11: LDA 1,5(7)	# set r1 to return address
12: ST 1,-1(5)	# store return address into printing's AR
13: ST 6,-7(5)	# save register 6 to AR
14: ST 5,-6(5)	# save register 5 to AR
15: ST 4,-5(5)	# save register 4 to AR
16: LDA 7,32(0)	# jump to printing
17: LD 1,-2(5)	# restore r1
18: LD 2,-3(5)	# restore r2
19: LD 3,-4(5)	# restore r3
20: LD 4,-5(5)	# restore r4
21: LD 6,-7(5)	# restore r6
22: LD 5,-6(5)	# restore r5
23: LD 2,0(5)	# put return value from printing into r2
24: ST 2,-8(5)	# move returned value into arg for PRINT's AR
25: LDA 3,2(7)	# put return address into r3
26: ST 3,-1(5)	# move return address into PRINT's AR
27: LDA 7,29(0)	# jump to PRINT
28: HALT 0,0,0
*
* PRINT
*
29: LD 1,-8(5)	# load arg from AR into r1
30: OUT 1,0,0	# print value
31: LD 7,-1(5)	# load return address into r7
*
* printing
*
32: LDC 1,8(0)	# load arg slot into r1
33: ST 1,0(0)	# store offset in frame
34: LD 1,0(0)	# load expr's temp value offset into r1
35: SUB 2,5,1	# get expr value's address in DMEM
36: LD 1,0(2)	# load expr value into r1
37: ST 6,-8(6)	# save register 6 to AR
38: ST 5,-7(6)	# save register 5 to AR
39: ST 4,-6(6)	# save register 4 to AR
40: ST 3,-5(6)	# save register 3 to AR
41: ST 2,-4(6)	# save register 2 to AR
42: ST 1,-3(6)	# save register 1 to AR
43: LDA 5,-1(6)	# set r5 to beginning of PRINT's AR
44: LDA 6,-7,5	# set r6 to end of PRINT's AR
45: SUB 4,5,6	# update current offset
46: ST 1,-8(5)	# put value to be printed into arg slot
47: LDA 6,-1(6)	# decrement stack pointer
48: LDA 4,1(4)	# increment offset
49: LDA 1,2(7)	# set r1 to return address
50: ST 1,-1(5)	# store return address into PRINT's AR
51: LDA 7,29(0)	# jump to PRINT
52: SUB 4,5,6	# update current offset
53: LD 1,-2(5)	# restore r1
54: LD 2,-3(5)	# restore r2
55: LD 3,-4(5)	# restore r3
56: LD 4,-5(5)	# restore r4
57: LD 6,-7(5)	# restore r6
58: LD 5,-6(5)	# restore r5
59: LDC 1,9(0)	# load arg slot into r1
60: ST 1,0(0)	# store offset in frame
61: LD 1,0(0)	# load expr's temp value offset into r1
62: SUB 2,5,1	# get expr value's address in DMEM
63: LD 1,0(2)	# load expr value into r1
64: ST 6,-8(6)	# save register 6 to AR
65: ST 5,-7(6)	# save register 5 to AR
66: ST 4,-6(6)	# save register 4 to AR
67: ST 3,-5(6)	# save register 3 to AR
68: ST 2,-4(6)	# save register 2 to AR
69: ST 1,-3(6)	# save register 1 to AR
70: LDA 5,-1(6)	# set r5 to beginning of PRINT's AR
71: LDA 6,-7,5	# set r6 to end of PRINT's AR
72: SUB 4,5,6	# update current offset
73: ST 1,-8(5)	# put value to be printed into arg slot
74: LDA 6,-1(6)	# decrement stack pointer
75: LDA 4,1(4)	# increment offset
76: LDA 1,2(7)	# set r1 to return address
77: ST 1,-1(5)	# store return address into PRINT's AR
78: LDA 7,29(0)	# jump to PRINT
79: SUB 4,5,6	# update current offset
80: LD 1,-2(5)	# restore r1
81: LD 2,-3(5)	# restore r2
82: LD 3,-4(5)	# restore r3
83: LD 4,-5(5)	# restore r4
84: LD 6,-7(5)	# restore r6
85: LD 5,-6(5)	# restore r5
86: ST 6,-8(6)	# save register 6 to AR
87: ST 5,-7(6)	# save register 5 to AR
88: ST 4,-6(6)	# save register 4 to AR
89: ST 3,-5(6)	# save register 3 to AR
90: ST 2,-4(6)	# save register 2 to AR
91: ST 1,-3(6)	# save register 1 to AR
92: LDA 5,-1(6)	# set r5 to beginning of sum's AR
93: LDA 6,-7,5	# set r6 to end of sum's AR
94: SUB 4,5,6	# update current offset
95: LD 5,-6(5)	# set r5 to last frame to get variable b
96: LD 1,-9(5)	# load variable b into r1
97: ST 1,-1(6)	# store value into new temp variable
98: LDA 6,-1(6)	# decrement end of stack pointer
99: LDA 4,1(4)	# increment offset
100: ADD 5,6,4	# set r5 back to next frame
101: ST 4,3(0)	# store offset in frame
102: LDA 6,-7(5)	# reset end of frame
103: SUB 4,5,6	# update current offset
104: LD 2,3(0)	# load arg1's offset into r2
105: SUB 3,5,2	# load temp arg1's address into r3
106: LD 2,0(3)	# load arg1 into r2
107: ST 2,-8(5)	# load arg1 into AR
108: LDA 6,-1(6)	# decrement end of stack pointer
109: SUB 4,5,6	# update current offset
110: LDA 1,2(7)	# set r1 to return address
111: ST 1,-1(5)	# store return address into sum's AR
112: LDA 7,156(0)	# jump to sum
113: SUB 4,5,6	# update current offset
114: LD 1,-2(5)	# restore r1
115: LD 2,-3(5)	# restore r2
116: LD 3,-4(5)	# restore r3
117: LD 4,-5(5)	# restore r4
118: LD 6,-7(5)	# restore r6
119: LD 5,-6(5)	# restore r5
120: LDA 6,-1(6)	# decrement end of stack pointer
121: SUB 4,5,6	# update current offset
122: ST 4,0(0)	# store offset in frame
123: LD 1,0(0)	# load expr's temp value offset into r1
124: SUB 2,5,1	# get expr value's address in DMEM
125: LD 1,0(2)	# load expr value into r1
126: ST 6,-8(6)	# save register 6 to AR
127: ST 5,-7(6)	# save register 5 to AR
128: ST 4,-6(6)	# save register 4 to AR
129: ST 3,-5(6)	# save register 3 to AR
130: ST 2,-4(6)	# save register 2 to AR
131: ST 1,-3(6)	# save register 1 to AR
132: LDA 5,-1(6)	# set r5 to beginning of PRINT's AR
133: LDA 6,-7,5	# set r6 to end of PRINT's AR
134: SUB 4,5,6	# update current offset
135: ST 1,-8(5)	# put value to be printed into arg slot
136: LDA 6,-1(6)	# decrement stack pointer
137: LDA 4,1(4)	# increment offset
138: LDA 1,2(7)	# set r1 to return address
139: ST 1,-1(5)	# store return address into PRINT's AR
140: LDA 7,29(0)	# jump to PRINT
141: SUB 4,5,6	# update current offset
142: LD 1,-2(5)	# restore r1
143: LD 2,-3(5)	# restore r2
144: LD 3,-4(5)	# restore r3
145: LD 4,-5(5)	# restore r4
146: LD 6,-7(5)	# restore r6
147: LD 5,-6(5)	# restore r5
148: LDC 1,0(0)	# load 0 into r1
149: ST 1,-1(6)	# copy r1 into new temp value
150: LDA 6,-1(6)	# decrement end of stack pointer
151: SUB 4,5,6	# update current offset
152: ST 4,0(0)	# store offset in frame
153: LD 1,0(6)	# load function's return value into r1
154: ST 1,0(5)	# put value from r1 into return value
155: LD 7,-1(5)	# load return address into r7
*
* sum
*
156: LDC 1,8(0)	# load arg slot into r1
157: ST 1,6(0)	# store offset in frame
158: LD 1,6(0)	# load left's temp value offset into r1
159: SUB 3,5,1	# get left value's address in DMEM
160: LDC 1,0(0)	# load 0 into r1
161: ST 1,-1(6)	# copy r1 into new temp value
162: LDA 6,-1(6)	# decrement end of stack pointer
163: SUB 4,5,6	# update current offset
164: ST 4,7(0)	# store offset in frame
165: LD 1,7(0)	# load right's temp value offset into r1
166: SUB 2,5,1	# get right value's address in DMEM
167: LD 1,0(3)	# load left operand value into r1
168: LD 2,0(2)	# load right operand value into r2
169: SUB 1,1,2	# subtract right operand from the left
170: JEQ 1,2(7)	# jump if left equals right
171: ST 0,-1(6)	# load false into new temp var
172: LDA 7,2(7)	# skip not equal
173: LDC 1,1(0)	# load 1 (true) into r1
174: ST 1,-1(6)	# load true into new temp var
175: LDA 6,-1(6)	# decrement end of stack pointer
176: SUB 4,5,6	# update current offset
177: ST 4,3(0)	# store offset in frame
178: LD 1,3(0)	# load ifExpr's temp value offset into r1
179: SUB 3,5,1	# get temp value's address in DMEM
180: LD 1,0(3)	# load ifExpr value into r1
181: JEQ 1,1(7)	# jump to else clause if false
182: LDA 7,2(7)	# jump to then clause
183: LDC 1,195(0)	# load else clause address
184: LDA 7,0(1)	# jump to else clause
185: LDC 1,0(0)	# load 0 into r1
186: ST 1,-1(6)	# copy r1 into new temp value
187: LDA 6,-1(6)	# decrement end of stack pointer
188: SUB 4,5,6	# update current offset
189: ST 4,4(0)	# store offset in frame
190: LD 1,4(0)	# load thenExpr's temp value offset into r1
191: SUB 3,5,1	# get temp value's address in DMEM
192: LD 2,0(3)	# load thenExpr value into r2
193: LDC 1,264(0)	# load end if address
194: LDA 7,0(1)	# jump over else clause to end if
195: LDC 1,8(0)	# load arg slot into r1
196: ST 1,6(0)	# store offset in frame
197: LD 1,6(0)	# load left's temp value offset into r1
198: SUB 3,5,1	# get left value's address in DMEM
199: ST 6,-8(6)	# save register 6 to AR
200: ST 5,-7(6)	# save register 5 to AR
201: ST 4,-6(6)	# save register 4 to AR
202: ST 3,-5(6)	# save register 3 to AR
203: ST 2,-4(6)	# save register 2 to AR
204: ST 1,-3(6)	# save register 1 to AR
205: LDA 5,-1(6)	# set r5 to beginning of sum's AR
206: LDA 6,-7,5	# set r6 to end of sum's AR
207: SUB 4,5,6	# update current offset
208: LD 5,-6(5)	# set r5 to last frame to get variable n
209: LD 1,-8(5)	# load variable n into r1
210: ST 1,-1(6)	# store value into new temp variable
211: LDA 6,-1(6)	# decrement end of stack pointer
212: LDA 4,1(4)	# increment offset
213: ADD 5,6,4	# set r5 back to next frame
214: ST 4,12(0)	# store offset in frame
215: LD 1,12(0)	# load left's temp value offset into r1
216: SUB 3,5,1	# get left value's address in DMEM
217: LDC 1,1(0)	# load 1 into r1
218: ST 1,-1(6)	# copy r1 into new temp value
219: LDA 6,-1(6)	# decrement end of stack pointer
220: SUB 4,5,6	# update current offset
221: ST 4,13(0)	# store offset in frame
222: LD 1,13(0)	# load right's temp value offset into r1
223: SUB 2,5,1	# get right value's address in DMEM
224: LD 1,0(3)	# load left operand value into r1
225: LD 2,0(2)	# load right operand value into r2
226: SUB 1,1,2	# subtract the two values
227: ST 1,-1(6)	# store difference into new temp value
228: LDA 6,-1(6)	# decrement end of stack pointer
229: SUB 4,5,6	# update current offset
230: ST 4,9(0)	# store offset in frame
231: LDA 6,-7(5)	# reset end of frame
232: SUB 4,5,6	# update current offset
233: LD 2,9(0)	# load arg1's offset into r2
234: SUB 3,5,2	# load temp arg1's address into r3
235: LD 2,0(3)	# load arg1 into r2
236: ST 2,-8(5)	# load arg1 into AR
237: LDA 6,-1(6)	# decrement end of stack pointer
238: SUB 4,5,6	# update current offset
239: LDA 1,2(7)	# set r1 to return address
240: ST 1,-1(5)	# store return address into sum's AR
241: LDA 7,156(0)	# jump to sum
242: SUB 4,5,6	# update current offset
243: LD 1,-2(5)	# restore r1
244: LD 2,-3(5)	# restore r2
245: LD 3,-4(5)	# restore r3
246: LD 4,-5(5)	# restore r4
247: LD 6,-7(5)	# restore r6
248: LD 5,-6(5)	# restore r5
249: LDA 6,-1(6)	# decrement end of stack pointer
250: SUB 4,5,6	# update current offset
251: ST 4,7(0)	# store offset in frame
252: LD 1,7(0)	# load right's temp value offset into r1
253: SUB 2,5,1	# get right value's address in DMEM
254: LD 1,0(3)	# load left operand value into r1
255: LD 2,0(2)	# load right operand value into r2
256: ADD 1,1,2	# add the two values
257: ST 1,-1(6)	# store sum into new temp value
258: LDA 6,-1(6)	# decrement end of stack pointer
259: SUB 4,5,6	# update current offset
260: ST 4,5(0)	# store offset in frame
261: LD 1,5(0)	# load elseExpr's temp value offset into r1
262: SUB 3,5,1	# get temp value's address in DMEM
263: LD 2,0(3)	# load elseExpr value into r2
264: ST 2,-1(6)	# store value to new temp value
265: LDA 6,-1(6)	# decrement end of stack pointer
266: SUB 4,5,6	# update current offset
267: ST 4,0(0)	# store offset in frame
268: LD 1,0(6)	# load function's return value into r1
269: ST 1,0(5)	# put value from r1 into return value
270: LD 7,-1(5)	# load return address into r7
