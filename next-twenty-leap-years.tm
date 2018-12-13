0: LD 5,0(0)	# set r5 to bottom of dmem
1: LDA 6,-7,5	# set r6 to end of NextTwentyLeapYears's AR
2: SUB 4,5,6	# update current offset
3: LD 2,1(0)	# load arg1 into r2
4: ST 2,-8(5)	# load arg1 into AR
5: LDA 6,-1(6)	# decrement end of stack pointer
6: SUB 4,5,6	# update current offset
7: LDA 1,5(7)	# set r1 to return address
8: ST 1,-1(5)	# store return address into NextTwentyLeapYears's AR
9: ST 6,-7(5)	# save register 6 to AR
10: ST 5,-6(5)	# save register 5 to AR
11: ST 4,-5(5)	# save register 4 to AR
12: LDA 7,28(0)	# jump to NextTwentyLeapYears
13: LD 1,-2(5)	# restore r1
14: LD 2,-3(5)	# restore r2
15: LD 3,-4(5)	# restore r3
16: LD 4,-5(5)	# restore r4
17: LD 6,-7(5)	# restore r6
18: LD 5,-6(5)	# restore r5
19: LD 2,0(5)	# put return value from NextTwentyLeapYears into r2
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
* NextTwentyLeapYears
*
28: ST 6,-8(6)	# save register 6 to AR
29: ST 5,-7(6)	# save register 5 to AR
30: ST 4,-6(6)	# save register 4 to AR
31: ST 3,-5(6)	# save register 3 to AR
32: ST 2,-4(6)	# save register 2 to AR
33: ST 1,-3(6)	# save register 1 to AR
34: LDA 5,-1(6)	# set r5 to beginning of getNextLeapYear's AR
35: LDA 6,-7,5	# set r6 to end of getNextLeapYear's AR
36: SUB 4,5,6	# update current offset
37: LD 5,-6(5)	# set r5 to last frame to get variable last
38: LD 1,-8(5)	# load variable last into r1
39: ST 1,-1(6)	# store value into new temp variable
40: LDA 6,-1(6)	# decrement end of stack pointer
41: LDA 4,1(4)	# increment offset
42: ADD 5,6,4	# set r5 back to next frame
43: ST 4,3(0)	# store offset in frame
44: LD 2,3(0)	# load arg1's offset into r2
45: SUB 3,5,2	# load temp arg1's address into r3
46: LD 2,0(3)	# load arg1 into r2
47: ST 2,-8(5)	# load arg1 into AR
48: LDC 1,20(0)	# load 20 into r1
49: ST 1,-1(6)	# copy r1 into new temp value
50: LDA 6,-1(6)	# decrement end of stack pointer
51: SUB 4,5,6	# update current offset
52: ST 4,4(0)	# store offset in frame
53: LD 2,4(0)	# load arg2's offset into r2
54: SUB 3,5,2	# load temp arg2's address into r3
55: LD 2,0(3)	# load arg2 into r2
56: ST 2,-9(5)	# load arg2 into AR
57: LDA 6,-9(5)	# reset end of frame to end of args
58: SUB 4,5,6	# update current offset
59: LDA 1,2(7)	# set r1 to return address
60: ST 1,-1(5)	# store return address into getNextLeapYear's AR
61: LDA 7,119(0)	# jump to getNextLeapYear
62: SUB 4,5,6	# update current offset
63: LD 1,-2(5)	# restore r1
64: LD 2,-3(5)	# restore r2
65: LD 3,-4(5)	# restore r3
66: LD 4,-5(5)	# restore r4
67: LD 6,-7(5)	# restore r6
68: LD 5,-6(5)	# restore r5
69: LDA 6,-1(6)	# decrement end of stack pointer
70: SUB 4,5,6	# update current offset
71: ST 4,0(0)	# store offset in frame
72: LD 1,0(6)	# load function's return value into r1
73: ST 1,0(5)	# put value from r1 into return value
74: LD 7,-1(5)	# load return address into r7
*
* MOD
*
75: LDC 1,9(0)	# load arg slot into r1
76: ST 1,3(0)	# store offset in frame
77: LD 1,3(0)	# load left's temp value offset into r1
78: SUB 3,5,1	# get left value's address in DMEM
79: LDC 1,9(0)	# load arg slot into r1
80: ST 1,9(0)	# store offset in frame
81: LD 1,9(0)	# load left's temp value offset into r1
82: SUB 3,5,1	# get left value's address in DMEM
83: LDC 1,8(0)	# load arg slot into r1
84: ST 1,10(0)	# store offset in frame
85: LD 1,10(0)	# load right's temp value offset into r1
86: SUB 2,5,1	# get right value's address in DMEM
87: LD 1,0(3)	# load left operand value into r1
88: LD 2,0(2)	# load right operand value into r2
89: DIV 1,1,2	# divide the r1 by r2
90: ST 1,-1(6)	# store quotient into new temp value
91: LDA 6,-1(6)	# decrement end of stack pointer
92: SUB 4,5,6	# update current offset
93: ST 4,6(0)	# store offset in frame
94: LD 1,6(0)	# load left's temp value offset into r1
95: SUB 3,5,1	# get left value's address in DMEM
96: LDC 1,8(0)	# load arg slot into r1
97: ST 1,7(0)	# store offset in frame
98: LD 1,7(0)	# load right's temp value offset into r1
99: SUB 2,5,1	# get right value's address in DMEM
100: LD 1,0(3)	# load left operand value into r1
101: LD 2,0(2)	# load right operand value into r2
102: MUL 1,1,2	# multiply the two values
103: ST 1,-1(6)	# store product into new temp value
104: LDA 6,-1(6)	# decrement end of stack pointer
105: SUB 4,5,6	# update current offset
106: ST 4,4(0)	# store offset in frame
107: LD 1,4(0)	# load right's temp value offset into r1
108: SUB 2,5,1	# get right value's address in DMEM
109: LD 1,0(3)	# load left operand value into r1
110: LD 2,0(2)	# load right operand value into r2
111: SUB 1,1,2	# subtract the two values
112: ST 1,-1(6)	# store difference into new temp value
113: LDA 6,-1(6)	# decrement end of stack pointer
114: SUB 4,5,6	# update current offset
115: ST 4,0(0)	# store offset in frame
116: LD 1,0(6)	# load function's return value into r1
117: ST 1,0(5)	# put value from r1 into return value
118: LD 7,-1(5)	# load return address into r7
*
* getNextLeapYear
*
119: LDC 1,2(0)	# load 2 into r1
120: ST 1,-1(6)	# copy r1 into new temp value
121: LDA 6,-1(6)	# decrement end of stack pointer
122: SUB 4,5,6	# update current offset
123: ST 4,6(0)	# store offset in frame
124: LD 1,6(0)	# load left's temp value offset into r1
125: SUB 3,5,1	# get left value's address in DMEM
126: LDC 1,9(0)	# load arg slot into r1
127: ST 1,7(0)	# store offset in frame
128: LD 1,7(0)	# load right's temp value offset into r1
129: SUB 2,5,1	# get right value's address in DMEM
130: LD 1,0(3)	# load left operand value into r1
131: LD 2,0(2)	# load right operand value into r2
132: SUB 1,1,2	# subtract right operand from the left
133: JLT 1,2(7)	# jump if left < right
134: ST 0,-1(6)	# load false into new temp var
135: LDA 7,2(7)	# skip not equal
136: LDC 1,1(0)	# load 1 (true) into r1
137: ST 1,-1(6)	# load true into new temp var
138: LDA 6,-1(6)	# decrement end of stack pointer
139: SUB 4,5,6	# update current offset
140: ST 4,3(0)	# store offset in frame
141: LD 1,3(0)	# load ifExpr's temp value offset into r1
142: SUB 3,5,1	# get temp value's address in DMEM
143: LD 1,0(3)	# load ifExpr value into r1
144: JEQ 1,1(7)	# jump to else clause if false
145: LDA 7,2(7)	# jump to then clause
146: LDC 1,231(0)	# load else clause address
147: LDA 7,0(1)	# jump to else clause
148: ST 6,-8(6)	# save register 6 to AR
149: ST 5,-7(6)	# save register 5 to AR
150: ST 4,-6(6)	# save register 4 to AR
151: ST 3,-5(6)	# save register 3 to AR
152: ST 2,-4(6)	# save register 2 to AR
153: ST 1,-3(6)	# save register 1 to AR
154: LDA 5,-1(6)	# set r5 to beginning of getNextLeapYear's AR
155: LDA 6,-7,5	# set r6 to end of getNextLeapYear's AR
156: SUB 4,5,6	# update current offset
157: LD 5,-6(5)	# set r5 to last frame to get variable n
158: LD 1,-8(5)	# load variable n into r1
159: ST 1,-1(6)	# store value into new temp variable
160: LDA 6,-1(6)	# decrement end of stack pointer
161: LDA 4,1(4)	# increment offset
162: ADD 5,6,4	# set r5 back to next frame
163: ST 4,9(0)	# store offset in frame
164: LD 1,9(0)	# load left's temp value offset into r1
165: SUB 3,5,1	# get left value's address in DMEM
166: LDC 1,4(0)	# load 4 into r1
167: ST 1,-1(6)	# copy r1 into new temp value
168: LDA 6,-1(6)	# decrement end of stack pointer
169: SUB 4,5,6	# update current offset
170: ST 4,10(0)	# store offset in frame
171: LD 1,10(0)	# load right's temp value offset into r1
172: SUB 2,5,1	# get right value's address in DMEM
173: LD 1,0(3)	# load left operand value into r1
174: LD 2,0(2)	# load right operand value into r2
175: ADD 1,1,2	# add the two values
176: ST 1,-1(6)	# store sum into new temp value
177: LDA 6,-1(6)	# decrement end of stack pointer
178: SUB 4,5,6	# update current offset
179: ST 4,6(0)	# store offset in frame
180: LD 2,6(0)	# load arg1's offset into r2
181: SUB 3,5,2	# load temp arg1's address into r3
182: LD 2,0(3)	# load arg1 into r2
183: ST 2,-8(5)	# load arg1 into AR
184: LD 5,-6(5)	# set r5 to last frame to get variable m
185: LD 1,-9(5)	# load variable m into r1
186: ST 1,-1(6)	# store value into new temp variable
187: LDA 6,-1(6)	# decrement end of stack pointer
188: LDA 4,1(4)	# increment offset
189: ADD 5,6,4	# set r5 back to next frame
190: ST 4,9(0)	# store offset in frame
191: LD 1,9(0)	# load left's temp value offset into r1
192: SUB 3,5,1	# get left value's address in DMEM
193: LDC 1,1(0)	# load 1 into r1
194: ST 1,-1(6)	# copy r1 into new temp value
195: LDA 6,-1(6)	# decrement end of stack pointer
196: SUB 4,5,6	# update current offset
197: ST 4,10(0)	# store offset in frame
198: LD 1,10(0)	# load right's temp value offset into r1
199: SUB 2,5,1	# get right value's address in DMEM
200: LD 1,0(3)	# load left operand value into r1
201: LD 2,0(2)	# load right operand value into r2
202: SUB 1,1,2	# subtract the two values
203: ST 1,-1(6)	# store difference into new temp value
204: LDA 6,-1(6)	# decrement end of stack pointer
205: SUB 4,5,6	# update current offset
206: ST 4,7(0)	# store offset in frame
207: LD 2,7(0)	# load arg2's offset into r2
208: SUB 3,5,2	# load temp arg2's address into r3
209: LD 2,0(3)	# load arg2 into r2
210: ST 2,-9(5)	# load arg2 into AR
211: LDA 6,-9(5)	# reset end of frame to end of args
212: SUB 4,5,6	# update current offset
213: LDA 1,2(7)	# set r1 to return address
214: ST 1,-1(5)	# store return address into getNextLeapYear's AR
215: LDA 7,119(0)	# jump to getNextLeapYear
216: SUB 4,5,6	# update current offset
217: LD 1,-2(5)	# restore r1
218: LD 2,-3(5)	# restore r2
219: LD 3,-4(5)	# restore r3
220: LD 4,-5(5)	# restore r4
221: LD 6,-7(5)	# restore r6
222: LD 5,-6(5)	# restore r5
223: LDA 6,-1(6)	# decrement end of stack pointer
224: SUB 4,5,6	# update current offset
225: ST 4,4(0)	# store offset in frame
226: LD 1,4(0)	# load thenExpr's temp value offset into r1
227: SUB 3,5,1	# get temp value's address in DMEM
228: LD 2,0(3)	# load thenExpr value into r2
229: LDC 1,417(0)	# load end if address
230: LDA 7,0(1)	# jump over else clause to end if
231: ST 6,-8(6)	# save register 6 to AR
232: ST 5,-7(6)	# save register 5 to AR
233: ST 4,-6(6)	# save register 4 to AR
234: ST 3,-5(6)	# save register 3 to AR
235: ST 2,-4(6)	# save register 2 to AR
236: ST 1,-3(6)	# save register 1 to AR
237: LDA 5,-1(6)	# set r5 to beginning of MOD's AR
238: LDA 6,-7,5	# set r6 to end of MOD's AR
239: SUB 4,5,6	# update current offset
240: LD 5,-6(5)	# set r5 to last frame to get variable n
241: LD 1,-8(5)	# load variable n into r1
242: ST 1,-1(6)	# store value into new temp variable
243: LDA 6,-1(6)	# decrement end of stack pointer
244: LDA 4,1(4)	# increment offset
245: ADD 5,6,4	# set r5 back to next frame
246: ST 4,12(0)	# store offset in frame
247: LD 2,12(0)	# load arg1's offset into r2
248: SUB 3,5,2	# load temp arg1's address into r3
249: LD 2,0(3)	# load arg1 into r2
250: ST 2,-8(5)	# load arg1 into AR
251: LDC 1,100(0)	# load 100 into r1
252: ST 1,-1(6)	# copy r1 into new temp value
253: LDA 6,-1(6)	# decrement end of stack pointer
254: SUB 4,5,6	# update current offset
255: ST 4,13(0)	# store offset in frame
256: LD 2,13(0)	# load arg2's offset into r2
257: SUB 3,5,2	# load temp arg2's address into r3
258: LD 2,0(3)	# load arg2 into r2
259: ST 2,-9(5)	# load arg2 into AR
260: LDA 6,-9(5)	# reset end of frame to end of args
261: SUB 4,5,6	# update current offset
262: LDA 1,2(7)	# set r1 to return address
263: ST 1,-1(5)	# store return address into MOD's AR
264: LDA 7,75(0)	# jump to MOD
265: SUB 4,5,6	# update current offset
266: LD 1,-2(5)	# restore r1
267: LD 2,-3(5)	# restore r2
268: LD 3,-4(5)	# restore r3
269: LD 4,-5(5)	# restore r4
270: LD 6,-7(5)	# restore r6
271: LD 5,-6(5)	# restore r5
272: LDA 6,-1(6)	# decrement end of stack pointer
273: SUB 4,5,6	# update current offset
274: ST 4,9(0)	# store offset in frame
275: LD 1,9(0)	# load left's temp value offset into r1
276: SUB 3,5,1	# get left value's address in DMEM
277: LDC 1,0(0)	# load 0 into r1
278: ST 1,-1(6)	# copy r1 into new temp value
279: LDA 6,-1(6)	# decrement end of stack pointer
280: SUB 4,5,6	# update current offset
281: ST 4,10(0)	# store offset in frame
282: LD 1,10(0)	# load right's temp value offset into r1
283: SUB 2,5,1	# get right value's address in DMEM
284: LD 1,0(3)	# load left operand value into r1
285: LD 2,0(2)	# load right operand value into r2
286: SUB 1,1,2	# subtract right operand from the left
287: JEQ 1,2(7)	# jump if left equals right
288: ST 0,-1(6)	# load false into new temp var
289: LDA 7,2(7)	# skip not equal
290: LDC 1,1(0)	# load 1 (true) into r1
291: ST 1,-1(6)	# load true into new temp var
292: LDA 6,-1(6)	# decrement end of stack pointer
293: SUB 4,5,6	# update current offset
294: ST 4,6(0)	# store offset in frame
295: LD 1,6(0)	# load ifExpr's temp value offset into r1
296: SUB 3,5,1	# get temp value's address in DMEM
297: LD 1,0(3)	# load ifExpr value into r1
298: JEQ 1,1(7)	# jump to else clause if false
299: LDA 7,2(7)	# jump to then clause
300: LDC 1,396(0)	# load else clause address
301: LDA 7,0(1)	# jump to else clause
302: ST 6,-8(6)	# save register 6 to AR
303: ST 5,-7(6)	# save register 5 to AR
304: ST 4,-6(6)	# save register 4 to AR
305: ST 3,-5(6)	# save register 3 to AR
306: ST 2,-4(6)	# save register 2 to AR
307: ST 1,-3(6)	# save register 1 to AR
308: LDA 5,-1(6)	# set r5 to beginning of MOD's AR
309: LDA 6,-7,5	# set r6 to end of MOD's AR
310: SUB 4,5,6	# update current offset
311: LD 5,-6(5)	# set r5 to last frame to get variable n
312: LD 1,-8(5)	# load variable n into r1
313: ST 1,-1(6)	# store value into new temp variable
314: LDA 6,-1(6)	# decrement end of stack pointer
315: LDA 4,1(4)	# increment offset
316: ADD 5,6,4	# set r5 back to next frame
317: ST 4,15(0)	# store offset in frame
318: LD 2,15(0)	# load arg1's offset into r2
319: SUB 3,5,2	# load temp arg1's address into r3
320: LD 2,0(3)	# load arg1 into r2
321: ST 2,-8(5)	# load arg1 into AR
322: LDC 1,400(0)	# load 400 into r1
323: ST 1,-1(6)	# copy r1 into new temp value
324: LDA 6,-1(6)	# decrement end of stack pointer
325: SUB 4,5,6	# update current offset
326: ST 4,16(0)	# store offset in frame
327: LD 2,16(0)	# load arg2's offset into r2
328: SUB 3,5,2	# load temp arg2's address into r3
329: LD 2,0(3)	# load arg2 into r2
330: ST 2,-9(5)	# load arg2 into AR
331: LDA 6,-9(5)	# reset end of frame to end of args
332: SUB 4,5,6	# update current offset
333: LDA 1,2(7)	# set r1 to return address
334: ST 1,-1(5)	# store return address into MOD's AR
335: LDA 7,75(0)	# jump to MOD
336: SUB 4,5,6	# update current offset
337: LD 1,-2(5)	# restore r1
338: LD 2,-3(5)	# restore r2
339: LD 3,-4(5)	# restore r3
340: LD 4,-5(5)	# restore r4
341: LD 6,-7(5)	# restore r6
342: LD 5,-6(5)	# restore r5
343: LDA 6,-1(6)	# decrement end of stack pointer
344: SUB 4,5,6	# update current offset
345: ST 4,12(0)	# store offset in frame
346: LD 1,12(0)	# load left's temp value offset into r1
347: SUB 3,5,1	# get left value's address in DMEM
348: LDC 1,0(0)	# load 0 into r1
349: ST 1,-1(6)	# copy r1 into new temp value
350: LDA 6,-1(6)	# decrement end of stack pointer
351: SUB 4,5,6	# update current offset
352: ST 4,13(0)	# store offset in frame
353: LD 1,13(0)	# load right's temp value offset into r1
354: SUB 2,5,1	# get right value's address in DMEM
355: LD 1,0(3)	# load left operand value into r1
356: LD 2,0(2)	# load right operand value into r2
357: SUB 1,1,2	# subtract right operand from the left
358: JEQ 1,2(7)	# jump if left equals right
359: ST 0,-1(6)	# load false into new temp var
360: LDA 7,2(7)	# skip not equal
361: LDC 1,1(0)	# load 1 (true) into r1
362: ST 1,-1(6)	# load true into new temp var
363: LDA 6,-1(6)	# decrement end of stack pointer
364: SUB 4,5,6	# update current offset
365: ST 4,9(0)	# store offset in frame
366: LD 1,9(0)	# load ifExpr's temp value offset into r1
367: SUB 3,5,1	# get temp value's address in DMEM
368: LD 1,0(3)	# load ifExpr value into r1
369: JEQ 1,1(7)	# jump to else clause if false
370: LDA 7,2(7)	# jump to then clause
371: LDC 1,426(0)	# load else clause address
372: LDA 7,0(1)	# jump to else clause
373: LDC 1,8(0)	# load arg slot into r1
374: ST 1,12(0)	# store offset in frame
375: LD 1,12(0)	# load left's temp value offset into r1
376: SUB 3,5,1	# get left value's address in DMEM
377: LDC 1,4(0)	# load 4 into r1
378: ST 1,-1(6)	# copy r1 into new temp value
379: LDA 6,-1(6)	# decrement end of stack pointer
380: SUB 4,5,6	# update current offset
381: ST 4,13(0)	# store offset in frame
382: LD 1,13(0)	# load right's temp value offset into r1
383: SUB 2,5,1	# get right value's address in DMEM
384: LD 1,0(3)	# load left operand value into r1
385: LD 2,0(2)	# load right operand value into r2
386: ADD 1,1,2	# add the two values
387: ST 1,-1(6)	# store sum into new temp value
388: LDA 6,-1(6)	# decrement end of stack pointer
389: SUB 4,5,6	# update current offset
390: ST 4,10(0)	# store offset in frame
391: LD 1,10(0)	# load thenExpr's temp value offset into r1
392: SUB 3,5,1	# get temp value's address in DMEM
393: LD 2,0(3)	# load thenExpr value into r2
394: LDC 1,454(0)	# load end if address
395: LDA 7,0(1)	# jump over else clause to end if
396: LDC 1,8(0)	# load arg slot into r1
397: ST 1,12(0)	# store offset in frame
398: LD 1,12(0)	# load left's temp value offset into r1
399: SUB 3,5,1	# get left value's address in DMEM
400: LDC 1,8(0)	# load 8 into r1
401: ST 1,-1(6)	# copy r1 into new temp value
402: LDA 6,-1(6)	# decrement end of stack pointer
403: SUB 4,5,6	# update current offset
404: ST 4,13(0)	# store offset in frame
405: LD 1,13(0)	# load right's temp value offset into r1
406: SUB 2,5,1	# get right value's address in DMEM
407: LD 1,0(3)	# load left operand value into r1
408: LD 2,0(2)	# load right operand value into r2
409: ADD 1,1,2	# add the two values
410: ST 1,-1(6)	# store sum into new temp value
411: LDA 6,-1(6)	# decrement end of stack pointer
412: SUB 4,5,6	# update current offset
413: ST 4,11(0)	# store offset in frame
414: LD 1,11(0)	# load elseExpr's temp value offset into r1
415: SUB 3,5,1	# get temp value's address in DMEM
416: LD 2,0(3)	# load elseExpr value into r2
417: ST 2,-1(6)	# store value to new temp value
418: LDA 6,-1(6)	# decrement end of stack pointer
419: SUB 4,5,6	# update current offset
420: ST 4,7(0)	# store offset in frame
421: LD 1,7(0)	# load thenExpr's temp value offset into r1
422: SUB 3,5,1	# get temp value's address in DMEM
423: LD 2,0(3)	# load thenExpr value into r2
424: LDC 1,447(0)	# load end if address
425: LDA 7,0(1)	# jump over else clause to end if
426: LDC 1,8(0)	# load arg slot into r1
427: ST 1,9(0)	# store offset in frame
428: LD 1,9(0)	# load left's temp value offset into r1
429: SUB 3,5,1	# get left value's address in DMEM
430: LDC 1,4(0)	# load 4 into r1
431: ST 1,-1(6)	# copy r1 into new temp value
432: LDA 6,-1(6)	# decrement end of stack pointer
433: SUB 4,5,6	# update current offset
434: ST 4,10(0)	# store offset in frame
435: LD 1,10(0)	# load right's temp value offset into r1
436: SUB 2,5,1	# get right value's address in DMEM
437: LD 1,0(3)	# load left operand value into r1
438: LD 2,0(2)	# load right operand value into r2
439: ADD 1,1,2	# add the two values
440: ST 1,-1(6)	# store sum into new temp value
441: LDA 6,-1(6)	# decrement end of stack pointer
442: SUB 4,5,6	# update current offset
443: ST 4,8(0)	# store offset in frame
444: LD 1,8(0)	# load elseExpr's temp value offset into r1
445: SUB 3,5,1	# get temp value's address in DMEM
446: LD 2,0(3)	# load elseExpr value into r2
447: ST 2,-1(6)	# store value to new temp value
448: LDA 6,-1(6)	# decrement end of stack pointer
449: SUB 4,5,6	# update current offset
450: ST 4,5(0)	# store offset in frame
451: LD 1,5(0)	# load elseExpr's temp value offset into r1
452: SUB 3,5,1	# get temp value's address in DMEM
453: LD 2,0(3)	# load elseExpr value into r2
454: ST 2,-1(6)	# store value to new temp value
455: LDA 6,-1(6)	# decrement end of stack pointer
456: SUB 4,5,6	# update current offset
457: ST 4,0(0)	# store offset in frame
458: LD 1,0(0)	# load expr's temp value offset into r1
459: SUB 2,5,1	# get expr value's address in DMEM
460: LD 1,0(2)	# load expr value into r1
461: ST 6,-8(6)	# save register 6 to AR
462: ST 5,-7(6)	# save register 5 to AR
463: ST 4,-6(6)	# save register 4 to AR
464: ST 3,-5(6)	# save register 3 to AR
465: ST 2,-4(6)	# save register 2 to AR
466: ST 1,-3(6)	# save register 1 to AR
467: LDA 5,-1(6)	# set r5 to beginning of PRINT's AR
468: LDA 6,-7,5	# set r6 to end of PRINT's AR
469: SUB 4,5,6	# update current offset
470: ST 1,-8(5)	# put value to be printed into arg slot
471: LDA 6,-1(6)	# decrement stack pointer
472: LDA 4,1(4)	# increment offset
473: LDA 1,2(7)	# set r1 to return address
474: ST 1,-1(5)	# store return address into PRINT's AR
475: LDA 7,25(0)	# jump to PRINT
476: SUB 4,5,6	# update current offset
477: LD 1,-2(5)	# restore r1
478: LD 2,-3(5)	# restore r2
479: LD 3,-4(5)	# restore r3
480: LD 4,-5(5)	# restore r4
481: LD 6,-7(5)	# restore r6
482: LD 5,-6(5)	# restore r5
483: LDC 1,9(0)	# load arg slot into r1
484: ST 1,6(0)	# store offset in frame
485: LD 1,6(0)	# load left's temp value offset into r1
486: SUB 3,5,1	# get left value's address in DMEM
487: LDC 1,1(0)	# load 1 into r1
488: ST 1,-1(6)	# copy r1 into new temp value
489: LDA 6,-1(6)	# decrement end of stack pointer
490: SUB 4,5,6	# update current offset
491: ST 4,7(0)	# store offset in frame
492: LD 1,7(0)	# load right's temp value offset into r1
493: SUB 2,5,1	# get right value's address in DMEM
494: LD 1,0(3)	# load left operand value into r1
495: LD 2,0(2)	# load right operand value into r2
496: SUB 1,1,2	# subtract right operand from the left
497: JEQ 1,2(7)	# jump if left equals right
498: ST 0,-1(6)	# load false into new temp var
499: LDA 7,2(7)	# skip not equal
500: LDC 1,1(0)	# load 1 (true) into r1
501: ST 1,-1(6)	# load true into new temp var
502: LDA 6,-1(6)	# decrement end of stack pointer
503: SUB 4,5,6	# update current offset
504: ST 4,3(0)	# store offset in frame
505: LD 1,3(0)	# load ifExpr's temp value offset into r1
506: SUB 3,5,1	# get temp value's address in DMEM
507: LD 1,0(3)	# load ifExpr value into r1
508: JEQ 1,1(7)	# jump to else clause if false
509: LDA 7,2(7)	# jump to then clause
510: LDC 1,677(0)	# load else clause address
511: LDA 7,0(1)	# jump to else clause
512: ST 6,-8(6)	# save register 6 to AR
513: ST 5,-7(6)	# save register 5 to AR
514: ST 4,-6(6)	# save register 4 to AR
515: ST 3,-5(6)	# save register 3 to AR
516: ST 2,-4(6)	# save register 2 to AR
517: ST 1,-3(6)	# save register 1 to AR
518: LDA 5,-1(6)	# set r5 to beginning of MOD's AR
519: LDA 6,-7,5	# set r6 to end of MOD's AR
520: SUB 4,5,6	# update current offset
521: LD 5,-6(5)	# set r5 to last frame to get variable n
522: LD 1,-8(5)	# load variable n into r1
523: ST 1,-1(6)	# store value into new temp variable
524: LDA 6,-1(6)	# decrement end of stack pointer
525: LDA 4,1(4)	# increment offset
526: ADD 5,6,4	# set r5 back to next frame
527: ST 4,12(0)	# store offset in frame
528: LD 2,12(0)	# load arg1's offset into r2
529: SUB 3,5,2	# load temp arg1's address into r3
530: LD 2,0(3)	# load arg1 into r2
531: ST 2,-8(5)	# load arg1 into AR
532: LDC 1,100(0)	# load 100 into r1
533: ST 1,-1(6)	# copy r1 into new temp value
534: LDA 6,-1(6)	# decrement end of stack pointer
535: SUB 4,5,6	# update current offset
536: ST 4,13(0)	# store offset in frame
537: LD 2,13(0)	# load arg2's offset into r2
538: SUB 3,5,2	# load temp arg2's address into r3
539: LD 2,0(3)	# load arg2 into r2
540: ST 2,-9(5)	# load arg2 into AR
541: LDA 6,-9(5)	# reset end of frame to end of args
542: SUB 4,5,6	# update current offset
543: LDA 1,2(7)	# set r1 to return address
544: ST 1,-1(5)	# store return address into MOD's AR
545: LDA 7,75(0)	# jump to MOD
546: SUB 4,5,6	# update current offset
547: LD 1,-2(5)	# restore r1
548: LD 2,-3(5)	# restore r2
549: LD 3,-4(5)	# restore r3
550: LD 4,-5(5)	# restore r4
551: LD 6,-7(5)	# restore r6
552: LD 5,-6(5)	# restore r5
553: LDA 6,-1(6)	# decrement end of stack pointer
554: SUB 4,5,6	# update current offset
555: ST 4,9(0)	# store offset in frame
556: LD 1,9(0)	# load left's temp value offset into r1
557: SUB 3,5,1	# get left value's address in DMEM
558: LDC 1,0(0)	# load 0 into r1
559: ST 1,-1(6)	# copy r1 into new temp value
560: LDA 6,-1(6)	# decrement end of stack pointer
561: SUB 4,5,6	# update current offset
562: ST 4,10(0)	# store offset in frame
563: LD 1,10(0)	# load right's temp value offset into r1
564: SUB 2,5,1	# get right value's address in DMEM
565: LD 1,0(3)	# load left operand value into r1
566: LD 2,0(2)	# load right operand value into r2
567: SUB 1,1,2	# subtract right operand from the left
568: JEQ 1,2(7)	# jump if left equals right
569: ST 0,-1(6)	# load false into new temp var
570: LDA 7,2(7)	# skip not equal
571: LDC 1,1(0)	# load 1 (true) into r1
572: ST 1,-1(6)	# load true into new temp var
573: LDA 6,-1(6)	# decrement end of stack pointer
574: SUB 4,5,6	# update current offset
575: ST 4,6(0)	# store offset in frame
576: LD 1,6(0)	# load ifExpr's temp value offset into r1
577: SUB 3,5,1	# get temp value's address in DMEM
578: LD 1,0(3)	# load ifExpr value into r1
579: JEQ 1,1(7)	# jump to else clause if false
580: LDA 7,2(7)	# jump to then clause
581: LDC 1,707(0)	# load else clause address
582: LDA 7,0(1)	# jump to else clause
583: ST 6,-8(6)	# save register 6 to AR
584: ST 5,-7(6)	# save register 5 to AR
585: ST 4,-6(6)	# save register 4 to AR
586: ST 3,-5(6)	# save register 3 to AR
587: ST 2,-4(6)	# save register 2 to AR
588: ST 1,-3(6)	# save register 1 to AR
589: LDA 5,-1(6)	# set r5 to beginning of MOD's AR
590: LDA 6,-7,5	# set r6 to end of MOD's AR
591: SUB 4,5,6	# update current offset
592: LD 5,-6(5)	# set r5 to last frame to get variable n
593: LD 1,-8(5)	# load variable n into r1
594: ST 1,-1(6)	# store value into new temp variable
595: LDA 6,-1(6)	# decrement end of stack pointer
596: LDA 4,1(4)	# increment offset
597: ADD 5,6,4	# set r5 back to next frame
598: ST 4,15(0)	# store offset in frame
599: LD 2,15(0)	# load arg1's offset into r2
600: SUB 3,5,2	# load temp arg1's address into r3
601: LD 2,0(3)	# load arg1 into r2
602: ST 2,-8(5)	# load arg1 into AR
603: LDC 1,400(0)	# load 400 into r1
604: ST 1,-1(6)	# copy r1 into new temp value
605: LDA 6,-1(6)	# decrement end of stack pointer
606: SUB 4,5,6	# update current offset
607: ST 4,16(0)	# store offset in frame
608: LD 2,16(0)	# load arg2's offset into r2
609: SUB 3,5,2	# load temp arg2's address into r3
610: LD 2,0(3)	# load arg2 into r2
611: ST 2,-9(5)	# load arg2 into AR
612: LDA 6,-9(5)	# reset end of frame to end of args
613: SUB 4,5,6	# update current offset
614: LDA 1,2(7)	# set r1 to return address
615: ST 1,-1(5)	# store return address into MOD's AR
616: LDA 7,75(0)	# jump to MOD
617: SUB 4,5,6	# update current offset
618: LD 1,-2(5)	# restore r1
619: LD 2,-3(5)	# restore r2
620: LD 3,-4(5)	# restore r3
621: LD 4,-5(5)	# restore r4
622: LD 6,-7(5)	# restore r6
623: LD 5,-6(5)	# restore r5
624: LDA 6,-1(6)	# decrement end of stack pointer
625: SUB 4,5,6	# update current offset
626: ST 4,12(0)	# store offset in frame
627: LD 1,12(0)	# load left's temp value offset into r1
628: SUB 3,5,1	# get left value's address in DMEM
629: LDC 1,0(0)	# load 0 into r1
630: ST 1,-1(6)	# copy r1 into new temp value
631: LDA 6,-1(6)	# decrement end of stack pointer
632: SUB 4,5,6	# update current offset
633: ST 4,13(0)	# store offset in frame
634: LD 1,13(0)	# load right's temp value offset into r1
635: SUB 2,5,1	# get right value's address in DMEM
636: LD 1,0(3)	# load left operand value into r1
637: LD 2,0(2)	# load right operand value into r2
638: SUB 1,1,2	# subtract right operand from the left
639: JEQ 1,2(7)	# jump if left equals right
640: ST 0,-1(6)	# load false into new temp var
641: LDA 7,2(7)	# skip not equal
642: LDC 1,1(0)	# load 1 (true) into r1
643: ST 1,-1(6)	# load true into new temp var
644: LDA 6,-1(6)	# decrement end of stack pointer
645: SUB 4,5,6	# update current offset
646: ST 4,9(0)	# store offset in frame
647: LD 1,9(0)	# load ifExpr's temp value offset into r1
648: SUB 3,5,1	# get temp value's address in DMEM
649: LD 1,0(3)	# load ifExpr value into r1
650: JEQ 1,1(7)	# jump to else clause if false
651: LDA 7,2(7)	# jump to then clause
652: LDC 1,737(0)	# load else clause address
653: LDA 7,0(1)	# jump to else clause
654: LDC 1,8(0)	# load arg slot into r1
655: ST 1,12(0)	# store offset in frame
656: LD 1,12(0)	# load left's temp value offset into r1
657: SUB 3,5,1	# get left value's address in DMEM
658: LDC 1,4(0)	# load 4 into r1
659: ST 1,-1(6)	# copy r1 into new temp value
660: LDA 6,-1(6)	# decrement end of stack pointer
661: SUB 4,5,6	# update current offset
662: ST 4,13(0)	# store offset in frame
663: LD 1,13(0)	# load right's temp value offset into r1
664: SUB 2,5,1	# get right value's address in DMEM
665: LD 1,0(3)	# load left operand value into r1
666: LD 2,0(2)	# load right operand value into r2
667: ADD 1,1,2	# add the two values
668: ST 1,-1(6)	# store sum into new temp value
669: LDA 6,-1(6)	# decrement end of stack pointer
670: SUB 4,5,6	# update current offset
671: ST 4,10(0)	# store offset in frame
672: LD 1,10(0)	# load thenExpr's temp value offset into r1
673: SUB 3,5,1	# get temp value's address in DMEM
674: LD 2,0(3)	# load thenExpr value into r2
675: LDC 1,818(0)	# load end if address
676: LDA 7,0(1)	# jump over else clause to end if
677: LDC 1,8(0)	# load arg slot into r1
678: ST 1,12(0)	# store offset in frame
679: LD 1,12(0)	# load left's temp value offset into r1
680: SUB 3,5,1	# get left value's address in DMEM
681: LDC 1,8(0)	# load 8 into r1
682: ST 1,-1(6)	# copy r1 into new temp value
683: LDA 6,-1(6)	# decrement end of stack pointer
684: SUB 4,5,6	# update current offset
685: ST 4,13(0)	# store offset in frame
686: LD 1,13(0)	# load right's temp value offset into r1
687: SUB 2,5,1	# get right value's address in DMEM
688: LD 1,0(3)	# load left operand value into r1
689: LD 2,0(2)	# load right operand value into r2
690: ADD 1,1,2	# add the two values
691: ST 1,-1(6)	# store sum into new temp value
692: LDA 6,-1(6)	# decrement end of stack pointer
693: SUB 4,5,6	# update current offset
694: ST 4,11(0)	# store offset in frame
695: LD 1,11(0)	# load elseExpr's temp value offset into r1
696: SUB 3,5,1	# get temp value's address in DMEM
697: LD 2,0(3)	# load elseExpr value into r2
698: ST 2,-1(6)	# store value to new temp value
699: LDA 6,-1(6)	# decrement end of stack pointer
700: SUB 4,5,6	# update current offset
701: ST 4,7(0)	# store offset in frame
702: LD 1,7(0)	# load thenExpr's temp value offset into r1
703: SUB 3,5,1	# get temp value's address in DMEM
704: LD 2,0(3)	# load thenExpr value into r2
705: LDC 1,728(0)	# load end if address
706: LDA 7,0(1)	# jump over else clause to end if
707: LDC 1,8(0)	# load arg slot into r1
708: ST 1,9(0)	# store offset in frame
709: LD 1,9(0)	# load left's temp value offset into r1
710: SUB 3,5,1	# get left value's address in DMEM
711: LDC 1,4(0)	# load 4 into r1
712: ST 1,-1(6)	# copy r1 into new temp value
713: LDA 6,-1(6)	# decrement end of stack pointer
714: SUB 4,5,6	# update current offset
715: ST 4,10(0)	# store offset in frame
716: LD 1,10(0)	# load right's temp value offset into r1
717: SUB 2,5,1	# get right value's address in DMEM
718: LD 1,0(3)	# load left operand value into r1
719: LD 2,0(2)	# load right operand value into r2
720: ADD 1,1,2	# add the two values
721: ST 1,-1(6)	# store sum into new temp value
722: LDA 6,-1(6)	# decrement end of stack pointer
723: SUB 4,5,6	# update current offset
724: ST 4,8(0)	# store offset in frame
725: LD 1,8(0)	# load elseExpr's temp value offset into r1
726: SUB 3,5,1	# get temp value's address in DMEM
727: LD 2,0(3)	# load elseExpr value into r2
728: ST 2,-1(6)	# store value to new temp value
729: LDA 6,-1(6)	# decrement end of stack pointer
730: SUB 4,5,6	# update current offset
731: ST 4,4(0)	# store offset in frame
732: LD 1,4(0)	# load thenExpr's temp value offset into r1
733: SUB 3,5,1	# get temp value's address in DMEM
734: LD 2,0(3)	# load thenExpr value into r2
735: LDC 1,698(0)	# load end if address
736: LDA 7,0(1)	# jump over else clause to end if
737: ST 6,-8(6)	# save register 6 to AR
738: ST 5,-7(6)	# save register 5 to AR
739: ST 4,-6(6)	# save register 4 to AR
740: ST 3,-5(6)	# save register 3 to AR
741: ST 2,-4(6)	# save register 2 to AR
742: ST 1,-3(6)	# save register 1 to AR
743: LDA 5,-1(6)	# set r5 to beginning of getNextLeapYear's AR
744: LDA 6,-7,5	# set r6 to end of getNextLeapYear's AR
745: SUB 4,5,6	# update current offset
746: LD 5,-6(5)	# set r5 to last frame to get variable n
747: LD 1,-8(5)	# load variable n into r1
748: ST 1,-1(6)	# store value into new temp variable
749: LDA 6,-1(6)	# decrement end of stack pointer
750: LDA 4,1(4)	# increment offset
751: ADD 5,6,4	# set r5 back to next frame
752: ST 4,9(0)	# store offset in frame
753: LD 1,9(0)	# load left's temp value offset into r1
754: SUB 3,5,1	# get left value's address in DMEM
755: LDC 1,4(0)	# load 4 into r1
756: ST 1,-1(6)	# copy r1 into new temp value
757: LDA 6,-1(6)	# decrement end of stack pointer
758: SUB 4,5,6	# update current offset
759: ST 4,10(0)	# store offset in frame
760: LD 1,10(0)	# load right's temp value offset into r1
761: SUB 2,5,1	# get right value's address in DMEM
762: LD 1,0(3)	# load left operand value into r1
763: LD 2,0(2)	# load right operand value into r2
764: ADD 1,1,2	# add the two values
765: ST 1,-1(6)	# store sum into new temp value
766: LDA 6,-1(6)	# decrement end of stack pointer
767: SUB 4,5,6	# update current offset
768: ST 4,6(0)	# store offset in frame
769: LD 2,6(0)	# load arg1's offset into r2
770: SUB 3,5,2	# load temp arg1's address into r3
771: LD 2,0(3)	# load arg1 into r2
772: ST 2,-8(5)	# load arg1 into AR
773: LD 5,-6(5)	# set r5 to last frame to get variable m
774: LD 1,-9(5)	# load variable m into r1
775: ST 1,-1(6)	# store value into new temp variable
776: LDA 6,-1(6)	# decrement end of stack pointer
777: LDA 4,1(4)	# increment offset
778: ADD 5,6,4	# set r5 back to next frame
779: ST 4,9(0)	# store offset in frame
780: LD 1,9(0)	# load left's temp value offset into r1
781: SUB 3,5,1	# get left value's address in DMEM
782: LDC 1,1(0)	# load 1 into r1
783: ST 1,-1(6)	# copy r1 into new temp value
784: LDA 6,-1(6)	# decrement end of stack pointer
785: SUB 4,5,6	# update current offset
786: ST 4,10(0)	# store offset in frame
787: LD 1,10(0)	# load right's temp value offset into r1
788: SUB 2,5,1	# get right value's address in DMEM
789: LD 1,0(3)	# load left operand value into r1
790: LD 2,0(2)	# load right operand value into r2
791: SUB 1,1,2	# subtract the two values
792: ST 1,-1(6)	# store difference into new temp value
793: LDA 6,-1(6)	# decrement end of stack pointer
794: SUB 4,5,6	# update current offset
795: ST 4,7(0)	# store offset in frame
796: LD 2,7(0)	# load arg2's offset into r2
797: SUB 3,5,2	# load temp arg2's address into r3
798: LD 2,0(3)	# load arg2 into r2
799: ST 2,-9(5)	# load arg2 into AR
800: LDA 6,-9(5)	# reset end of frame to end of args
801: SUB 4,5,6	# update current offset
802: LDA 1,2(7)	# set r1 to return address
803: ST 1,-1(5)	# store return address into getNextLeapYear's AR
804: LDA 7,119(0)	# jump to getNextLeapYear
805: SUB 4,5,6	# update current offset
806: LD 1,-2(5)	# restore r1
807: LD 2,-3(5)	# restore r2
808: LD 3,-4(5)	# restore r3
809: LD 4,-5(5)	# restore r4
810: LD 6,-7(5)	# restore r6
811: LD 5,-6(5)	# restore r5
812: LDA 6,-1(6)	# decrement end of stack pointer
813: SUB 4,5,6	# update current offset
814: ST 4,5(0)	# store offset in frame
815: LD 1,5(0)	# load elseExpr's temp value offset into r1
816: SUB 3,5,1	# get temp value's address in DMEM
817: LD 2,0(3)	# load elseExpr value into r2
818: ST 2,-1(6)	# store value to new temp value
819: LDA 6,-1(6)	# decrement end of stack pointer
820: SUB 4,5,6	# update current offset
821: ST 4,0(0)	# store offset in frame
822: LD 1,0(6)	# load function's return value into r1
823: ST 1,0(5)	# put value from r1 into return value
824: LD 7,-1(5)	# load return address into r7
