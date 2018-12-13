0: LD 5,0(0)	# set r5 to bottom of dmem
1: LDA 6,-7,5	# set r6 to end of IsPrime's AR
2: SUB 4,5,6	# update current offset
3: LD 2,1(0)	# load arg1 into r2
4: ST 2,-8(5)	# load arg1 into AR
5: LDA 6,-1(6)	# decrement end of stack pointer
6: SUB 4,5,6	# update current offset
7: LDA 1,5(7)	# set r1 to return address
8: ST 1,-1(5)	# store return address into IsPrime's AR
9: ST 6,-7(5)	# save register 6 to AR
10: ST 5,-6(5)	# save register 5 to AR
11: ST 4,-5(5)	# save register 4 to AR
12: LDA 7,28(0)	# jump to IsPrime
13: LD 1,-2(5)	# restore r1
14: LD 2,-3(5)	# restore r2
15: LD 3,-4(5)	# restore r3
16: LD 4,-5(5)	# restore r4
17: LD 6,-7(5)	# restore r6
18: LD 5,-6(5)	# restore r5
19: LD 2,0(5)	# put return value from IsPrime into r2
20: ST 2,-8(5)	# move returned value into arg for PRINT's AR
21: LDA 3,2(7)	# put return address into r3
22: ST 3,-1(5)	# move return address into PRINT's AR
23: LDA 7,25(0)	# jump to PRINT
24: HALT 0,0,0
*
* PRINT
*
25: LD 1,-8(5)	# load arg from AR into r1
26: OUT 1,0,0	# print value
27: LD 7,-1(5)	# load return address into r7
*
* IsPrime
*
28: ST 6,-8(6)	# save register 6 to AR
29: ST 5,-7(6)	# save register 5 to AR
30: ST 4,-6(6)	# save register 4 to AR
31: ST 3,-5(6)	# save register 3 to AR
32: ST 2,-4(6)	# save register 2 to AR
33: ST 1,-3(6)	# save register 1 to AR
34: LDA 5,-1(6)	# set r5 to beginning of isPrime's AR
35: LDA 6,-7,5	# set r6 to end of isPrime's AR
36: SUB 4,5,6	# update current offset
37: LD 5,-6(5)	# set r5 to last frame to get variable n
38: LD 1,-8(5)	# load variable n into r1
39: ST 1,-1(6)	# store value into new temp variable
40: LDA 6,-1(6)	# decrement end of stack pointer
41: LDA 4,1(4)	# increment offset
42: ADD 5,6,4	# set r5 back to next frame
43: ST 4,6(0)	# store offset in frame
44: LD 2,6(0)	# load arg1's offset into r2
45: SUB 3,5,2	# load temp arg1's address into r3
46: LD 2,0(3)	# load arg1 into r2
47: ST 2,-8(5)	# load arg1 into AR
48: LD 5,-6(5)	# set r5 to last frame to get variable n
49: LD 1,-8(5)	# load variable n into r1
50: ST 1,-1(6)	# store value into new temp variable
51: LDA 6,-1(6)	# decrement end of stack pointer
52: LDA 4,1(4)	# increment offset
53: ADD 5,6,4	# set r5 back to next frame
54: ST 4,9(0)	# store offset in frame
55: LD 1,9(0)	# load left's temp value offset into r1
56: SUB 3,5,1	# get left value's address in DMEM
57: LDC 1,1(0)	# load 1 into r1
58: ST 1,-1(6)	# copy r1 into new temp value
59: LDA 6,-1(6)	# decrement end of stack pointer
60: SUB 4,5,6	# update current offset
61: ST 4,10(0)	# store offset in frame
62: LD 1,10(0)	# load right's temp value offset into r1
63: SUB 2,5,1	# get right value's address in DMEM
64: LD 1,0(3)	# load left operand value into r1
65: LD 2,0(2)	# load right operand value into r2
66: SUB 1,1,2	# subtract the two values
67: ST 1,-1(6)	# store difference into new temp value
68: LDA 6,-1(6)	# decrement end of stack pointer
69: SUB 4,5,6	# update current offset
70: ST 4,7(0)	# store offset in frame
71: LD 2,7(0)	# load arg2's offset into r2
72: SUB 3,5,2	# load temp arg2's address into r3
73: LD 2,0(3)	# load arg2 into r2
74: ST 2,-9(5)	# load arg2 into AR
75: LDA 6,-9(5)	# reset end of frame to end of args
76: SUB 4,5,6	# update current offset
77: LDA 1,2(7)	# set r1 to return address
78: ST 1,-1(5)	# store return address into isPrime's AR
79: LDA 7,166(0)	# jump to isPrime
80: SUB 4,5,6	# update current offset
81: LD 1,-2(5)	# restore r1
82: LD 2,-3(5)	# restore r2
83: LD 3,-4(5)	# restore r3
84: LD 4,-5(5)	# restore r4
85: LD 6,-7(5)	# restore r6
86: LD 5,-6(5)	# restore r5
87: LDA 6,-1(6)	# decrement end of stack pointer
88: SUB 4,5,6	# update current offset
89: ST 4,3(0)	# store offset in frame
90: LD 1,3(0)	# load ifExpr's temp value offset into r1
91: SUB 3,5,1	# get temp value's address in DMEM
92: LD 1,0(3)	# load ifExpr value into r1
93: JEQ 1,1(7)	# jump to else clause if false
94: LDA 7,2(7)	# jump to then clause
95: LDC 1,107(0)	# load else clause address
96: LDA 7,0(1)	# jump to else clause
97: LDC 1,1(0)	# load 1 into r1
98: ST 1,-1(6)	# copy r1 into new temp value
99: LDA 6,-1(6)	# decrement end of stack pointer
100: SUB 4,5,6	# update current offset
101: ST 4,4(0)	# store offset in frame
102: LD 1,4(0)	# load thenExpr's temp value offset into r1
103: SUB 3,5,1	# get temp value's address in DMEM
104: LD 2,0(3)	# load thenExpr value into r2
105: LDC 1,115(0)	# load end if address
106: LDA 7,0(1)	# jump over else clause to end if
107: LDC 1,0(0)	# load 0 into r1
108: ST 1,-1(6)	# copy r1 into new temp value
109: LDA 6,-1(6)	# decrement end of stack pointer
110: SUB 4,5,6	# update current offset
111: ST 4,5(0)	# store offset in frame
112: LD 1,5(0)	# load elseExpr's temp value offset into r1
113: SUB 3,5,1	# get temp value's address in DMEM
114: LD 2,0(3)	# load elseExpr value into r2
115: ST 2,-1(6)	# store value to new temp value
116: LDA 6,-1(6)	# decrement end of stack pointer
117: SUB 4,5,6	# update current offset
118: ST 4,0(0)	# store offset in frame
119: LD 1,0(6)	# load function's return value into r1
120: ST 1,0(5)	# put value from r1 into return value
121: LD 7,-1(5)	# load return address into r7
*
* MOD
*
122: LDC 1,9(0)	# load arg slot into r1
123: ST 1,3(0)	# store offset in frame
124: LD 1,3(0)	# load left's temp value offset into r1
125: SUB 3,5,1	# get left value's address in DMEM
126: LDC 1,9(0)	# load arg slot into r1
127: ST 1,9(0)	# store offset in frame
128: LD 1,9(0)	# load left's temp value offset into r1
129: SUB 3,5,1	# get left value's address in DMEM
130: LDC 1,8(0)	# load arg slot into r1
131: ST 1,10(0)	# store offset in frame
132: LD 1,10(0)	# load right's temp value offset into r1
133: SUB 2,5,1	# get right value's address in DMEM
134: LD 1,0(3)	# load left operand value into r1
135: LD 2,0(2)	# load right operand value into r2
136: DIV 1,1,2	# divide the r1 by r2
137: ST 1,-1(6)	# store quotient into new temp value
138: LDA 6,-1(6)	# decrement end of stack pointer
139: SUB 4,5,6	# update current offset
140: ST 4,6(0)	# store offset in frame
141: LD 1,6(0)	# load left's temp value offset into r1
142: SUB 3,5,1	# get left value's address in DMEM
143: LDC 1,8(0)	# load arg slot into r1
144: ST 1,7(0)	# store offset in frame
145: LD 1,7(0)	# load right's temp value offset into r1
146: SUB 2,5,1	# get right value's address in DMEM
147: LD 1,0(3)	# load left operand value into r1
148: LD 2,0(2)	# load right operand value into r2
149: MUL 1,1,2	# multiply the two values
150: ST 1,-1(6)	# store product into new temp value
151: LDA 6,-1(6)	# decrement end of stack pointer
152: SUB 4,5,6	# update current offset
153: ST 4,4(0)	# store offset in frame
154: LD 1,4(0)	# load right's temp value offset into r1
155: SUB 2,5,1	# get right value's address in DMEM
156: LD 1,0(3)	# load left operand value into r1
157: LD 2,0(2)	# load right operand value into r2
158: SUB 1,1,2	# subtract the two values
159: ST 1,-1(6)	# store difference into new temp value
160: LDA 6,-1(6)	# decrement end of stack pointer
161: SUB 4,5,6	# update current offset
162: ST 4,0(0)	# store offset in frame
163: LD 1,0(6)	# load function's return value into r1
164: ST 1,0(5)	# put value from r1 into return value
165: LD 7,-1(5)	# load return address into r7
*
* isPrime
*
166: LDC 1,9(0)	# load arg slot into r1
167: ST 1,6(0)	# store offset in frame
168: LD 1,6(0)	# load left's temp value offset into r1
169: SUB 3,5,1	# get left value's address in DMEM
170: LDC 1,1(0)	# load 1 into r1
171: ST 1,-1(6)	# copy r1 into new temp value
172: LDA 6,-1(6)	# decrement end of stack pointer
173: SUB 4,5,6	# update current offset
174: ST 4,7(0)	# store offset in frame
175: LD 1,7(0)	# load right's temp value offset into r1
176: SUB 2,5,1	# get right value's address in DMEM
177: LD 1,0(3)	# load left operand value into r1
178: LD 2,0(2)	# load right operand value into r2
179: SUB 1,1,2	# subtract right operand from the left
180: JEQ 1,2(7)	# jump if left equals right
181: ST 0,-1(6)	# load false into new temp var
182: LDA 7,2(7)	# skip not equal
183: LDC 1,1(0)	# load 1 (true) into r1
184: ST 1,-1(6)	# load true into new temp var
185: LDA 6,-1(6)	# decrement end of stack pointer
186: SUB 4,5,6	# update current offset
187: ST 4,3(0)	# store offset in frame
188: LD 1,3(0)	# load ifExpr's temp value offset into r1
189: SUB 3,5,1	# get temp value's address in DMEM
190: LD 1,0(3)	# load ifExpr value into r1
191: JEQ 1,1(7)	# jump to else clause if false
192: LDA 7,2(7)	# jump to then clause
193: LDC 1,205(0)	# load else clause address
194: LDA 7,0(1)	# jump to else clause
195: LDC 1,1(0)	# load 1 (true) into r1
196: ST 1,-1(6)	# copy r1 into new temp value
197: LDA 6,-1(6)	# decrement end of stack pointer
198: SUB 4,5,6	# update current offset
199: ST 4,4(0)	# store offset in frame
200: LD 1,4(0)	# load thenExpr's temp value offset into r1
201: SUB 3,5,1	# get temp value's address in DMEM
202: LD 2,0(3)	# load thenExpr value into r2
203: LDC 1,353(0)	# load end if address
204: LDA 7,0(1)	# jump over else clause to end if
205: ST 6,-8(6)	# save register 6 to AR
206: ST 5,-7(6)	# save register 5 to AR
207: ST 4,-6(6)	# save register 4 to AR
208: ST 3,-5(6)	# save register 3 to AR
209: ST 2,-4(6)	# save register 2 to AR
210: ST 1,-3(6)	# save register 1 to AR
211: LDA 5,-1(6)	# set r5 to beginning of MOD's AR
212: LDA 6,-7,5	# set r6 to end of MOD's AR
213: SUB 4,5,6	# update current offset
214: LD 5,-6(5)	# set r5 to last frame to get variable n
215: LD 1,-8(5)	# load variable n into r1
216: ST 1,-1(6)	# store value into new temp variable
217: LDA 6,-1(6)	# decrement end of stack pointer
218: LDA 4,1(4)	# increment offset
219: ADD 5,6,4	# set r5 back to next frame
220: ST 4,12(0)	# store offset in frame
221: LD 2,12(0)	# load arg1's offset into r2
222: SUB 3,5,2	# load temp arg1's address into r3
223: LD 2,0(3)	# load arg1 into r2
224: ST 2,-8(5)	# load arg1 into AR
225: LD 5,-6(5)	# set r5 to last frame to get variable divisor
226: LD 1,-9(5)	# load variable divisor into r1
227: ST 1,-1(6)	# store value into new temp variable
228: LDA 6,-1(6)	# decrement end of stack pointer
229: LDA 4,1(4)	# increment offset
230: ADD 5,6,4	# set r5 back to next frame
231: ST 4,13(0)	# store offset in frame
232: LD 2,13(0)	# load arg2's offset into r2
233: SUB 3,5,2	# load temp arg2's address into r3
234: LD 2,0(3)	# load arg2 into r2
235: ST 2,-9(5)	# load arg2 into AR
236: LDA 6,-9(5)	# reset end of frame to end of args
237: SUB 4,5,6	# update current offset
238: LDA 1,2(7)	# set r1 to return address
239: ST 1,-1(5)	# store return address into MOD's AR
240: LDA 7,122(0)	# jump to MOD
241: SUB 4,5,6	# update current offset
242: LD 1,-2(5)	# restore r1
243: LD 2,-3(5)	# restore r2
244: LD 3,-4(5)	# restore r3
245: LD 4,-5(5)	# restore r4
246: LD 6,-7(5)	# restore r6
247: LD 5,-6(5)	# restore r5
248: LDA 6,-1(6)	# decrement end of stack pointer
249: SUB 4,5,6	# update current offset
250: ST 4,9(0)	# store offset in frame
251: LD 1,9(0)	# load left's temp value offset into r1
252: SUB 3,5,1	# get left value's address in DMEM
253: LDC 1,0(0)	# load 0 into r1
254: ST 1,-1(6)	# copy r1 into new temp value
255: LDA 6,-1(6)	# decrement end of stack pointer
256: SUB 4,5,6	# update current offset
257: ST 4,10(0)	# store offset in frame
258: LD 1,10(0)	# load right's temp value offset into r1
259: SUB 2,5,1	# get right value's address in DMEM
260: LD 1,0(3)	# load left operand value into r1
261: LD 2,0(2)	# load right operand value into r2
262: SUB 1,1,2	# subtract right operand from the left
263: JEQ 1,2(7)	# jump if left equals right
264: ST 0,-1(6)	# load false into new temp var
265: LDA 7,2(7)	# skip not equal
266: LDC 1,1(0)	# load 1 (true) into r1
267: ST 1,-1(6)	# load true into new temp var
268: LDA 6,-1(6)	# decrement end of stack pointer
269: SUB 4,5,6	# update current offset
270: ST 4,6(0)	# store offset in frame
271: LD 1,6(0)	# load ifExpr's temp value offset into r1
272: SUB 3,5,1	# get temp value's address in DMEM
273: LD 1,0(3)	# load ifExpr value into r1
274: JEQ 1,1(7)	# jump to else clause if false
275: LDA 7,2(7)	# jump to then clause
276: LDC 1,288(0)	# load else clause address
277: LDA 7,0(1)	# jump to else clause
278: LDC 1,0(0)	# load 0 (false) into r1
279: ST 1,-1(6)	# copy r1 into new temp value
280: LDA 6,-1(6)	# decrement end of stack pointer
281: SUB 4,5,6	# update current offset
282: ST 4,7(0)	# store offset in frame
283: LD 1,7(0)	# load thenExpr's temp value offset into r1
284: SUB 3,5,1	# get temp value's address in DMEM
285: LD 2,0(3)	# load thenExpr value into r2
286: LDC 1,360(0)	# load end if address
287: LDA 7,0(1)	# jump over else clause to end if
288: ST 6,-8(6)	# save register 6 to AR
289: ST 5,-7(6)	# save register 5 to AR
290: ST 4,-6(6)	# save register 4 to AR
291: ST 3,-5(6)	# save register 3 to AR
292: ST 2,-4(6)	# save register 2 to AR
293: ST 1,-3(6)	# save register 1 to AR
294: LDA 5,-1(6)	# set r5 to beginning of isPrime's AR
295: LDA 6,-7,5	# set r6 to end of isPrime's AR
296: SUB 4,5,6	# update current offset
297: LD 5,-6(5)	# set r5 to last frame to get variable n
298: LD 1,-8(5)	# load variable n into r1
299: ST 1,-1(6)	# store value into new temp variable
300: LDA 6,-1(6)	# decrement end of stack pointer
301: LDA 4,1(4)	# increment offset
302: ADD 5,6,4	# set r5 back to next frame
303: ST 4,9(0)	# store offset in frame
304: LD 2,9(0)	# load arg1's offset into r2
305: SUB 3,5,2	# load temp arg1's address into r3
306: LD 2,0(3)	# load arg1 into r2
307: ST 2,-8(5)	# load arg1 into AR
308: LD 5,-6(5)	# set r5 to last frame to get variable divisor
309: LD 1,-9(5)	# load variable divisor into r1
310: ST 1,-1(6)	# store value into new temp variable
311: LDA 6,-1(6)	# decrement end of stack pointer
312: LDA 4,1(4)	# increment offset
313: ADD 5,6,4	# set r5 back to next frame
314: ST 4,12(0)	# store offset in frame
315: LD 1,12(0)	# load left's temp value offset into r1
316: SUB 3,5,1	# get left value's address in DMEM
317: LDC 1,1(0)	# load 1 into r1
318: ST 1,-1(6)	# copy r1 into new temp value
319: LDA 6,-1(6)	# decrement end of stack pointer
320: SUB 4,5,6	# update current offset
321: ST 4,13(0)	# store offset in frame
322: LD 1,13(0)	# load right's temp value offset into r1
323: SUB 2,5,1	# get right value's address in DMEM
324: LD 1,0(3)	# load left operand value into r1
325: LD 2,0(2)	# load right operand value into r2
326: SUB 1,1,2	# subtract the two values
327: ST 1,-1(6)	# store difference into new temp value
328: LDA 6,-1(6)	# decrement end of stack pointer
329: SUB 4,5,6	# update current offset
330: ST 4,10(0)	# store offset in frame
331: LD 2,10(0)	# load arg2's offset into r2
332: SUB 3,5,2	# load temp arg2's address into r3
333: LD 2,0(3)	# load arg2 into r2
334: ST 2,-9(5)	# load arg2 into AR
335: LDA 6,-9(5)	# reset end of frame to end of args
336: SUB 4,5,6	# update current offset
337: LDA 1,2(7)	# set r1 to return address
338: ST 1,-1(5)	# store return address into isPrime's AR
339: LDA 7,166(0)	# jump to isPrime
340: SUB 4,5,6	# update current offset
341: LD 1,-2(5)	# restore r1
342: LD 2,-3(5)	# restore r2
343: LD 3,-4(5)	# restore r3
344: LD 4,-5(5)	# restore r4
345: LD 6,-7(5)	# restore r6
346: LD 5,-6(5)	# restore r5
347: LDA 6,-1(6)	# decrement end of stack pointer
348: SUB 4,5,6	# update current offset
349: ST 4,8(0)	# store offset in frame
350: LD 1,8(0)	# load elseExpr's temp value offset into r1
351: SUB 3,5,1	# get temp value's address in DMEM
352: LD 2,0(3)	# load elseExpr value into r2
353: ST 2,-1(6)	# store value to new temp value
354: LDA 6,-1(6)	# decrement end of stack pointer
355: SUB 4,5,6	# update current offset
356: ST 4,5(0)	# store offset in frame
357: LD 1,5(0)	# load elseExpr's temp value offset into r1
358: SUB 3,5,1	# get temp value's address in DMEM
359: LD 2,0(3)	# load elseExpr value into r2
360: ST 2,-1(6)	# store value to new temp value
361: LDA 6,-1(6)	# decrement end of stack pointer
362: SUB 4,5,6	# update current offset
363: ST 4,0(0)	# store offset in frame
364: LD 1,0(6)	# load function's return value into r1
365: ST 1,0(5)	# put value from r1 into return value
366: LD 7,-1(5)	# load return address into r7
