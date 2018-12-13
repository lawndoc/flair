0: LD 5,0(0)	# set r5 to bottom of dmem
1: LDA 6,-7,5	# set r6 to end of factors's AR
2: SUB 4,5,6	# update current offset
3: LD 2,1(0)	# load arg1 into r2
4: ST 2,-8(5)	# load arg1 into AR
5: LDA 6,-1(6)	# decrement end of stack pointer
6: SUB 4,5,6	# update current offset
7: LDA 1,5(7)	# set r1 to return address
8: ST 1,-1(5)	# store return address into factors's AR
9: ST 6,-7(5)	# save register 6 to AR
10: ST 5,-6(5)	# save register 5 to AR
11: ST 4,-5(5)	# save register 4 to AR
12: LDA 7,28(0)	# jump to factors
13: LD 1,-2(5)	# restore r1
14: LD 2,-3(5)	# restore r2
15: LD 3,-4(5)	# restore r3
16: LD 4,-5(5)	# restore r4
17: LD 6,-7(5)	# restore r6
18: LD 5,-6(5)	# restore r5
19: LD 2,0(5)	# put return value from factors into r2
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
* factors
*
28: ST 6,-8(6)	# save register 6 to AR
29: ST 5,-7(6)	# save register 5 to AR
30: ST 4,-6(6)	# save register 4 to AR
31: ST 3,-5(6)	# save register 3 to AR
32: ST 2,-4(6)	# save register 2 to AR
33: ST 1,-3(6)	# save register 1 to AR
34: LDA 5,-1(6)	# set r5 to beginning of loopToN's AR
35: LDA 6,-7,5	# set r6 to end of loopToN's AR
36: SUB 4,5,6	# update current offset
37: LD 5,-6(5)	# set r5 to last frame to get variable n
38: LD 1,-8(5)	# load variable n into r1
39: ST 1,-1(6)	# store value into new temp variable
40: LDA 6,-1(6)	# decrement end of stack pointer
41: LDA 4,1(4)	# increment offset
42: ADD 5,6,4	# set r5 back to next frame
43: ST 4,3(0)	# store offset in frame
44: LD 2,3(0)	# load arg1's offset into r2
45: SUB 3,5,2	# load temp arg1's address into r3
46: LD 2,0(3)	# load arg1 into r2
47: ST 2,-8(5)	# load arg1 into AR
48: LDC 1,1(0)	# load 1 into r1
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
60: ST 1,-1(5)	# store return address into loopToN's AR
61: LDA 7,75(0)	# jump to loopToN
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
* loopToN
*
75: LDC 1,8(0)	# load arg slot into r1
76: ST 1,6(0)	# store offset in frame
77: LD 1,6(0)	# load left's temp value offset into r1
78: SUB 3,5,1	# get left value's address in DMEM
79: LDC 1,9(0)	# load arg slot into r1
80: ST 1,7(0)	# store offset in frame
81: LD 1,7(0)	# load right's temp value offset into r1
82: SUB 2,5,1	# get right value's address in DMEM
83: LD 1,0(3)	# load left operand value into r1
84: LD 2,0(2)	# load right operand value into r2
85: SUB 1,1,2	# subtract right operand from the left
86: JEQ 1,2(7)	# jump if left equals right
87: ST 0,-1(6)	# load false into new temp var
88: LDA 7,2(7)	# skip not equal
89: LDC 1,1(0)	# load 1 (true) into r1
90: ST 1,-1(6)	# load true into new temp var
91: LDA 6,-1(6)	# decrement end of stack pointer
92: SUB 4,5,6	# update current offset
93: ST 4,3(0)	# store offset in frame
94: LD 1,3(0)	# load ifExpr's temp value offset into r1
95: SUB 3,5,1	# get temp value's address in DMEM
96: LD 1,0(3)	# load ifExpr value into r1
97: JEQ 1,1(7)	# jump to else clause if false
98: LDA 7,2(7)	# jump to then clause
99: LDC 1,108(0)	# load else clause address
100: LDA 7,0(1)	# jump to else clause
101: LDC 1,8(0)	# load arg slot into r1
102: ST 1,4(0)	# store offset in frame
103: LD 1,4(0)	# load thenExpr's temp value offset into r1
104: SUB 3,5,1	# get temp value's address in DMEM
105: LD 2,0(3)	# load thenExpr value into r2
106: LDC 1,157(0)	# load end if address
107: LDA 7,0(1)	# jump over else clause to end if
108: ST 6,-8(6)	# save register 6 to AR
109: ST 5,-7(6)	# save register 5 to AR
110: ST 4,-6(6)	# save register 4 to AR
111: ST 3,-5(6)	# save register 3 to AR
112: ST 2,-4(6)	# save register 2 to AR
113: ST 1,-3(6)	# save register 1 to AR
114: LDA 5,-1(6)	# set r5 to beginning of testAndLoop's AR
115: LDA 6,-7,5	# set r6 to end of testAndLoop's AR
116: SUB 4,5,6	# update current offset
117: LD 5,-6(5)	# set r5 to last frame to get variable n
118: LD 1,-8(5)	# load variable n into r1
119: ST 1,-1(6)	# store value into new temp variable
120: LDA 6,-1(6)	# decrement end of stack pointer
121: LDA 4,1(4)	# increment offset
122: ADD 5,6,4	# set r5 back to next frame
123: ST 4,6(0)	# store offset in frame
124: LD 2,6(0)	# load arg1's offset into r2
125: SUB 3,5,2	# load temp arg1's address into r3
126: LD 2,0(3)	# load arg1 into r2
127: ST 2,-8(5)	# load arg1 into AR
128: LD 5,-6(5)	# set r5 to last frame to get variable current
129: LD 1,-9(5)	# load variable current into r1
130: ST 1,-1(6)	# store value into new temp variable
131: LDA 6,-1(6)	# decrement end of stack pointer
132: LDA 4,1(4)	# increment offset
133: ADD 5,6,4	# set r5 back to next frame
134: ST 4,7(0)	# store offset in frame
135: LD 2,7(0)	# load arg2's offset into r2
136: SUB 3,5,2	# load temp arg2's address into r3
137: LD 2,0(3)	# load arg2 into r2
138: ST 2,-9(5)	# load arg2 into AR
139: LDA 6,-9(5)	# reset end of frame to end of args
140: SUB 4,5,6	# update current offset
141: LDA 1,2(7)	# set r1 to return address
142: ST 1,-1(5)	# store return address into testAndLoop's AR
143: LDA 7,164(0)	# jump to testAndLoop
144: SUB 4,5,6	# update current offset
145: LD 1,-2(5)	# restore r1
146: LD 2,-3(5)	# restore r2
147: LD 3,-4(5)	# restore r3
148: LD 4,-5(5)	# restore r4
149: LD 6,-7(5)	# restore r6
150: LD 5,-6(5)	# restore r5
151: LDA 6,-1(6)	# decrement end of stack pointer
152: SUB 4,5,6	# update current offset
153: ST 4,5(0)	# store offset in frame
154: LD 1,5(0)	# load elseExpr's temp value offset into r1
155: SUB 3,5,1	# get temp value's address in DMEM
156: LD 2,0(3)	# load elseExpr value into r2
157: ST 2,-1(6)	# store value to new temp value
158: LDA 6,-1(6)	# decrement end of stack pointer
159: SUB 4,5,6	# update current offset
160: ST 4,0(0)	# store offset in frame
161: LD 1,0(6)	# load function's return value into r1
162: ST 1,0(5)	# put value from r1 into return value
163: LD 7,-1(5)	# load return address into r7
*
* testAndLoop
*
164: ST 6,-8(6)	# save register 6 to AR
165: ST 5,-7(6)	# save register 5 to AR
166: ST 4,-6(6)	# save register 4 to AR
167: ST 3,-5(6)	# save register 3 to AR
168: ST 2,-4(6)	# save register 2 to AR
169: ST 1,-3(6)	# save register 1 to AR
170: LDA 5,-1(6)	# set r5 to beginning of divides's AR
171: LDA 6,-7,5	# set r6 to end of divides's AR
172: SUB 4,5,6	# update current offset
173: LD 5,-6(5)	# set r5 to last frame to get variable current
174: LD 1,-9(5)	# load variable current into r1
175: ST 1,-1(6)	# store value into new temp variable
176: LDA 6,-1(6)	# decrement end of stack pointer
177: LDA 4,1(4)	# increment offset
178: ADD 5,6,4	# set r5 back to next frame
179: ST 4,6(0)	# store offset in frame
180: LD 2,6(0)	# load arg1's offset into r2
181: SUB 3,5,2	# load temp arg1's address into r3
182: LD 2,0(3)	# load arg1 into r2
183: ST 2,-8(5)	# load arg1 into AR
184: LD 5,-6(5)	# set r5 to last frame to get variable n
185: LD 1,-8(5)	# load variable n into r1
186: ST 1,-1(6)	# store value into new temp variable
187: LDA 6,-1(6)	# decrement end of stack pointer
188: LDA 4,1(4)	# increment offset
189: ADD 5,6,4	# set r5 back to next frame
190: ST 4,7(0)	# store offset in frame
191: LD 2,7(0)	# load arg2's offset into r2
192: SUB 3,5,2	# load temp arg2's address into r3
193: LD 2,0(3)	# load arg2 into r2
194: ST 2,-9(5)	# load arg2 into AR
195: LDA 6,-9(5)	# reset end of frame to end of args
196: SUB 4,5,6	# update current offset
197: LDA 1,2(7)	# set r1 to return address
198: ST 1,-1(5)	# store return address into divides's AR
199: LDA 7,432(0)	# jump to divides
200: SUB 4,5,6	# update current offset
201: LD 1,-2(5)	# restore r1
202: LD 2,-3(5)	# restore r2
203: LD 3,-4(5)	# restore r3
204: LD 4,-5(5)	# restore r4
205: LD 6,-7(5)	# restore r6
206: LD 5,-6(5)	# restore r5
207: LDA 6,-1(6)	# decrement end of stack pointer
208: SUB 4,5,6	# update current offset
209: ST 4,3(0)	# store offset in frame
210: LD 1,3(0)	# load ifExpr's temp value offset into r1
211: SUB 3,5,1	# get temp value's address in DMEM
212: LD 1,0(3)	# load ifExpr value into r1
213: JEQ 1,1(7)	# jump to else clause if false
214: LDA 7,2(7)	# jump to then clause
215: LDC 1,268(0)	# load else clause address
216: LDA 7,0(1)	# jump to else clause
217: ST 6,-8(6)	# save register 6 to AR
218: ST 5,-7(6)	# save register 5 to AR
219: ST 4,-6(6)	# save register 4 to AR
220: ST 3,-5(6)	# save register 3 to AR
221: ST 2,-4(6)	# save register 2 to AR
222: ST 1,-3(6)	# save register 1 to AR
223: LDA 5,-1(6)	# set r5 to beginning of printAndLoop's AR
224: LDA 6,-7,5	# set r6 to end of printAndLoop's AR
225: SUB 4,5,6	# update current offset
226: LD 5,-6(5)	# set r5 to last frame to get variable n
227: LD 1,-8(5)	# load variable n into r1
228: ST 1,-1(6)	# store value into new temp variable
229: LDA 6,-1(6)	# decrement end of stack pointer
230: LDA 4,1(4)	# increment offset
231: ADD 5,6,4	# set r5 back to next frame
232: ST 4,6(0)	# store offset in frame
233: LD 2,6(0)	# load arg1's offset into r2
234: SUB 3,5,2	# load temp arg1's address into r3
235: LD 2,0(3)	# load arg1 into r2
236: ST 2,-8(5)	# load arg1 into AR
237: LD 5,-6(5)	# set r5 to last frame to get variable current
238: LD 1,-9(5)	# load variable current into r1
239: ST 1,-1(6)	# store value into new temp variable
240: LDA 6,-1(6)	# decrement end of stack pointer
241: LDA 4,1(4)	# increment offset
242: ADD 5,6,4	# set r5 back to next frame
243: ST 4,7(0)	# store offset in frame
244: LD 2,7(0)	# load arg2's offset into r2
245: SUB 3,5,2	# load temp arg2's address into r3
246: LD 2,0(3)	# load arg2 into r2
247: ST 2,-9(5)	# load arg2 into AR
248: LDA 6,-9(5)	# reset end of frame to end of args
249: SUB 4,5,6	# update current offset
250: LDA 1,2(7)	# set r1 to return address
251: ST 1,-1(5)	# store return address into printAndLoop's AR
252: LDA 7,340(0)	# jump to printAndLoop
253: SUB 4,5,6	# update current offset
254: LD 1,-2(5)	# restore r1
255: LD 2,-3(5)	# restore r2
256: LD 3,-4(5)	# restore r3
257: LD 4,-5(5)	# restore r4
258: LD 6,-7(5)	# restore r6
259: LD 5,-6(5)	# restore r5
260: LDA 6,-1(6)	# decrement end of stack pointer
261: SUB 4,5,6	# update current offset
262: ST 4,4(0)	# store offset in frame
263: LD 1,4(0)	# load thenExpr's temp value offset into r1
264: SUB 3,5,1	# get temp value's address in DMEM
265: LD 2,0(3)	# load thenExpr value into r2
266: LDC 1,333(0)	# load end if address
267: LDA 7,0(1)	# jump over else clause to end if
268: ST 6,-8(6)	# save register 6 to AR
269: ST 5,-7(6)	# save register 5 to AR
270: ST 4,-6(6)	# save register 4 to AR
271: ST 3,-5(6)	# save register 3 to AR
272: ST 2,-4(6)	# save register 2 to AR
273: ST 1,-3(6)	# save register 1 to AR
274: LDA 5,-1(6)	# set r5 to beginning of loopToN's AR
275: LDA 6,-7,5	# set r6 to end of loopToN's AR
276: SUB 4,5,6	# update current offset
277: LD 5,-6(5)	# set r5 to last frame to get variable n
278: LD 1,-8(5)	# load variable n into r1
279: ST 1,-1(6)	# store value into new temp variable
280: LDA 6,-1(6)	# decrement end of stack pointer
281: LDA 4,1(4)	# increment offset
282: ADD 5,6,4	# set r5 back to next frame
283: ST 4,6(0)	# store offset in frame
284: LD 2,6(0)	# load arg1's offset into r2
285: SUB 3,5,2	# load temp arg1's address into r3
286: LD 2,0(3)	# load arg1 into r2
287: ST 2,-8(5)	# load arg1 into AR
288: LD 5,-6(5)	# set r5 to last frame to get variable current
289: LD 1,-9(5)	# load variable current into r1
290: ST 1,-1(6)	# store value into new temp variable
291: LDA 6,-1(6)	# decrement end of stack pointer
292: LDA 4,1(4)	# increment offset
293: ADD 5,6,4	# set r5 back to next frame
294: ST 4,9(0)	# store offset in frame
295: LD 1,9(0)	# load left's temp value offset into r1
296: SUB 3,5,1	# get left value's address in DMEM
297: LDC 1,1(0)	# load 1 into r1
298: ST 1,-1(6)	# copy r1 into new temp value
299: LDA 6,-1(6)	# decrement end of stack pointer
300: SUB 4,5,6	# update current offset
301: ST 4,10(0)	# store offset in frame
302: LD 1,10(0)	# load right's temp value offset into r1
303: SUB 2,5,1	# get right value's address in DMEM
304: LD 1,0(3)	# load left operand value into r1
305: LD 2,0(2)	# load right operand value into r2
306: ADD 1,1,2	# add the two values
307: ST 1,-1(6)	# store sum into new temp value
308: LDA 6,-1(6)	# decrement end of stack pointer
309: SUB 4,5,6	# update current offset
310: ST 4,7(0)	# store offset in frame
311: LD 2,7(0)	# load arg2's offset into r2
312: SUB 3,5,2	# load temp arg2's address into r3
313: LD 2,0(3)	# load arg2 into r2
314: ST 2,-9(5)	# load arg2 into AR
315: LDA 6,-9(5)	# reset end of frame to end of args
316: SUB 4,5,6	# update current offset
317: LDA 1,2(7)	# set r1 to return address
318: ST 1,-1(5)	# store return address into loopToN's AR
319: LDA 7,75(0)	# jump to loopToN
320: SUB 4,5,6	# update current offset
321: LD 1,-2(5)	# restore r1
322: LD 2,-3(5)	# restore r2
323: LD 3,-4(5)	# restore r3
324: LD 4,-5(5)	# restore r4
325: LD 6,-7(5)	# restore r6
326: LD 5,-6(5)	# restore r5
327: LDA 6,-1(6)	# decrement end of stack pointer
328: SUB 4,5,6	# update current offset
329: ST 4,5(0)	# store offset in frame
330: LD 1,5(0)	# load elseExpr's temp value offset into r1
331: SUB 3,5,1	# get temp value's address in DMEM
332: LD 2,0(3)	# load elseExpr value into r2
333: ST 2,-1(6)	# store value to new temp value
334: LDA 6,-1(6)	# decrement end of stack pointer
335: SUB 4,5,6	# update current offset
336: ST 4,0(0)	# store offset in frame
337: LD 1,0(6)	# load function's return value into r1
338: ST 1,0(5)	# put value from r1 into return value
339: LD 7,-1(5)	# load return address into r7
*
* printAndLoop
*
340: LDC 1,9(0)	# load arg slot into r1
341: ST 1,0(0)	# store offset in frame
342: LD 1,0(0)	# load expr's temp value offset into r1
343: SUB 2,5,1	# get expr value's address in DMEM
344: LD 1,0(2)	# load expr value into r1
345: ST 6,-8(6)	# save register 6 to AR
346: ST 5,-7(6)	# save register 5 to AR
347: ST 4,-6(6)	# save register 4 to AR
348: ST 3,-5(6)	# save register 3 to AR
349: ST 2,-4(6)	# save register 2 to AR
350: ST 1,-3(6)	# save register 1 to AR
351: LDA 5,-1(6)	# set r5 to beginning of PRINT's AR
352: LDA 6,-7,5	# set r6 to end of PRINT's AR
353: SUB 4,5,6	# update current offset
354: ST 1,-8(5)	# put value to be printed into arg slot
355: LDA 6,-1(6)	# decrement stack pointer
356: LDA 4,1(4)	# increment offset
357: LDA 1,2(7)	# set r1 to return address
358: ST 1,-1(5)	# store return address into PRINT's AR
359: LDA 7,25(0)	# jump to PRINT
360: SUB 4,5,6	# update current offset
361: LD 1,-2(5)	# restore r1
362: LD 2,-3(5)	# restore r2
363: LD 3,-4(5)	# restore r3
364: LD 4,-5(5)	# restore r4
365: LD 6,-7(5)	# restore r6
366: LD 5,-6(5)	# restore r5
367: ST 6,-8(6)	# save register 6 to AR
368: ST 5,-7(6)	# save register 5 to AR
369: ST 4,-6(6)	# save register 4 to AR
370: ST 3,-5(6)	# save register 3 to AR
371: ST 2,-4(6)	# save register 2 to AR
372: ST 1,-3(6)	# save register 1 to AR
373: LDA 5,-1(6)	# set r5 to beginning of loopToN's AR
374: LDA 6,-7,5	# set r6 to end of loopToN's AR
375: SUB 4,5,6	# update current offset
376: LD 5,-6(5)	# set r5 to last frame to get variable n
377: LD 1,-8(5)	# load variable n into r1
378: ST 1,-1(6)	# store value into new temp variable
379: LDA 6,-1(6)	# decrement end of stack pointer
380: LDA 4,1(4)	# increment offset
381: ADD 5,6,4	# set r5 back to next frame
382: ST 4,3(0)	# store offset in frame
383: LD 2,3(0)	# load arg1's offset into r2
384: SUB 3,5,2	# load temp arg1's address into r3
385: LD 2,0(3)	# load arg1 into r2
386: ST 2,-8(5)	# load arg1 into AR
387: LD 5,-6(5)	# set r5 to last frame to get variable current
388: LD 1,-9(5)	# load variable current into r1
389: ST 1,-1(6)	# store value into new temp variable
390: LDA 6,-1(6)	# decrement end of stack pointer
391: LDA 4,1(4)	# increment offset
392: ADD 5,6,4	# set r5 back to next frame
393: ST 4,6(0)	# store offset in frame
394: LD 1,6(0)	# load left's temp value offset into r1
395: SUB 3,5,1	# get left value's address in DMEM
396: LDC 1,1(0)	# load 1 into r1
397: ST 1,-1(6)	# copy r1 into new temp value
398: LDA 6,-1(6)	# decrement end of stack pointer
399: SUB 4,5,6	# update current offset
400: ST 4,7(0)	# store offset in frame
401: LD 1,7(0)	# load right's temp value offset into r1
402: SUB 2,5,1	# get right value's address in DMEM
403: LD 1,0(3)	# load left operand value into r1
404: LD 2,0(2)	# load right operand value into r2
405: ADD 1,1,2	# add the two values
406: ST 1,-1(6)	# store sum into new temp value
407: LDA 6,-1(6)	# decrement end of stack pointer
408: SUB 4,5,6	# update current offset
409: ST 4,4(0)	# store offset in frame
410: LD 2,4(0)	# load arg2's offset into r2
411: SUB 3,5,2	# load temp arg2's address into r3
412: LD 2,0(3)	# load arg2 into r2
413: ST 2,-9(5)	# load arg2 into AR
414: LDA 6,-9(5)	# reset end of frame to end of args
415: SUB 4,5,6	# update current offset
416: LDA 1,2(7)	# set r1 to return address
417: ST 1,-1(5)	# store return address into loopToN's AR
418: LDA 7,75(0)	# jump to loopToN
419: SUB 4,5,6	# update current offset
420: LD 1,-2(5)	# restore r1
421: LD 2,-3(5)	# restore r2
422: LD 3,-4(5)	# restore r3
423: LD 4,-5(5)	# restore r4
424: LD 6,-7(5)	# restore r6
425: LD 5,-6(5)	# restore r5
426: LDA 6,-1(6)	# decrement end of stack pointer
427: SUB 4,5,6	# update current offset
428: ST 4,0(0)	# store offset in frame
429: LD 1,0(6)	# load function's return value into r1
430: ST 1,0(5)	# put value from r1 into return value
431: LD 7,-1(5)	# load return address into r7
*
* divides
*
432: ST 6,-8(6)	# save register 6 to AR
433: ST 5,-7(6)	# save register 5 to AR
434: ST 4,-6(6)	# save register 4 to AR
435: ST 3,-5(6)	# save register 3 to AR
436: ST 2,-4(6)	# save register 2 to AR
437: ST 1,-3(6)	# save register 1 to AR
438: LDA 5,-1(6)	# set r5 to beginning of remainder's AR
439: LDA 6,-7,5	# set r6 to end of remainder's AR
440: SUB 4,5,6	# update current offset
441: LD 5,-6(5)	# set r5 to last frame to get variable b
442: LD 1,-9(5)	# load variable b into r1
443: ST 1,-1(6)	# store value into new temp variable
444: LDA 6,-1(6)	# decrement end of stack pointer
445: LDA 4,1(4)	# increment offset
446: ADD 5,6,4	# set r5 back to next frame
447: ST 4,6(0)	# store offset in frame
448: LD 2,6(0)	# load arg1's offset into r2
449: SUB 3,5,2	# load temp arg1's address into r3
450: LD 2,0(3)	# load arg1 into r2
451: ST 2,-8(5)	# load arg1 into AR
452: LD 5,-6(5)	# set r5 to last frame to get variable a
453: LD 1,-8(5)	# load variable a into r1
454: ST 1,-1(6)	# store value into new temp variable
455: LDA 6,-1(6)	# decrement end of stack pointer
456: LDA 4,1(4)	# increment offset
457: ADD 5,6,4	# set r5 back to next frame
458: ST 4,7(0)	# store offset in frame
459: LD 2,7(0)	# load arg2's offset into r2
460: SUB 3,5,2	# load temp arg2's address into r3
461: LD 2,0(3)	# load arg2 into r2
462: ST 2,-9(5)	# load arg2 into AR
463: LDA 6,-9(5)	# reset end of frame to end of args
464: SUB 4,5,6	# update current offset
465: LDA 1,2(7)	# set r1 to return address
466: ST 1,-1(5)	# store return address into remainder's AR
467: LDA 7,501(0)	# jump to remainder
468: SUB 4,5,6	# update current offset
469: LD 1,-2(5)	# restore r1
470: LD 2,-3(5)	# restore r2
471: LD 3,-4(5)	# restore r3
472: LD 4,-5(5)	# restore r4
473: LD 6,-7(5)	# restore r6
474: LD 5,-6(5)	# restore r5
475: LDA 6,-1(6)	# decrement end of stack pointer
476: SUB 4,5,6	# update current offset
477: ST 4,3(0)	# store offset in frame
478: LD 1,3(0)	# load left's temp value offset into r1
479: SUB 3,5,1	# get left value's address in DMEM
480: LDC 1,0(0)	# load 0 into r1
481: ST 1,-1(6)	# copy r1 into new temp value
482: LDA 6,-1(6)	# decrement end of stack pointer
483: SUB 4,5,6	# update current offset
484: ST 4,4(0)	# store offset in frame
485: LD 1,4(0)	# load right's temp value offset into r1
486: SUB 2,5,1	# get right value's address in DMEM
487: LD 1,0(3)	# load left operand value into r1
488: LD 2,0(2)	# load right operand value into r2
489: SUB 1,1,2	# subtract right operand from the left
490: JEQ 1,2(7)	# jump if left equals right
491: ST 0,-1(6)	# load false into new temp var
492: LDA 7,2(7)	# skip not equal
493: LDC 1,1(0)	# load 1 (true) into r1
494: ST 1,-1(6)	# load true into new temp var
495: LDA 6,-1(6)	# decrement end of stack pointer
496: SUB 4,5,6	# update current offset
497: ST 4,0(0)	# store offset in frame
498: LD 1,0(6)	# load function's return value into r1
499: ST 1,0(5)	# put value from r1 into return value
500: LD 7,-1(5)	# load return address into r7
*
* remainder
*
501: LDC 1,8(0)	# load arg slot into r1
502: ST 1,6(0)	# store offset in frame
503: LD 1,6(0)	# load left's temp value offset into r1
504: SUB 3,5,1	# get left value's address in DMEM
505: LDC 1,9(0)	# load arg slot into r1
506: ST 1,7(0)	# store offset in frame
507: LD 1,7(0)	# load right's temp value offset into r1
508: SUB 2,5,1	# get right value's address in DMEM
509: LD 1,0(3)	# load left operand value into r1
510: LD 2,0(2)	# load right operand value into r2
511: SUB 1,1,2	# subtract right operand from the left
512: JLT 1,2(7)	# jump if left < right
513: ST 0,-1(6)	# load false into new temp var
514: LDA 7,2(7)	# skip not equal
515: LDC 1,1(0)	# load 1 (true) into r1
516: ST 1,-1(6)	# load true into new temp var
517: LDA 6,-1(6)	# decrement end of stack pointer
518: SUB 4,5,6	# update current offset
519: ST 4,3(0)	# store offset in frame
520: LD 1,3(0)	# load ifExpr's temp value offset into r1
521: SUB 3,5,1	# get temp value's address in DMEM
522: LD 1,0(3)	# load ifExpr value into r1
523: JEQ 1,1(7)	# jump to else clause if false
524: LDA 7,2(7)	# jump to then clause
525: LDC 1,534(0)	# load else clause address
526: LDA 7,0(1)	# jump to else clause
527: LDC 1,8(0)	# load arg slot into r1
528: ST 1,4(0)	# store offset in frame
529: LD 1,4(0)	# load thenExpr's temp value offset into r1
530: SUB 3,5,1	# get temp value's address in DMEM
531: LD 2,0(3)	# load thenExpr value into r2
532: LDC 1,601(0)	# load end if address
533: LDA 7,0(1)	# jump over else clause to end if
534: ST 6,-8(6)	# save register 6 to AR
535: ST 5,-7(6)	# save register 5 to AR
536: ST 4,-6(6)	# save register 4 to AR
537: ST 3,-5(6)	# save register 3 to AR
538: ST 2,-4(6)	# save register 2 to AR
539: ST 1,-3(6)	# save register 1 to AR
540: LDA 5,-1(6)	# set r5 to beginning of remainder's AR
541: LDA 6,-7,5	# set r6 to end of remainder's AR
542: SUB 4,5,6	# update current offset
543: LD 5,-6(5)	# set r5 to last frame to get variable num
544: LD 1,-8(5)	# load variable num into r1
545: ST 1,-1(6)	# store value into new temp variable
546: LDA 6,-1(6)	# decrement end of stack pointer
547: LDA 4,1(4)	# increment offset
548: ADD 5,6,4	# set r5 back to next frame
549: ST 4,9(0)	# store offset in frame
550: LD 1,9(0)	# load left's temp value offset into r1
551: SUB 3,5,1	# get left value's address in DMEM
552: LD 5,-6(5)	# set r5 to last frame to get variable den
553: LD 1,-9(5)	# load variable den into r1
554: ST 1,-1(6)	# store value into new temp variable
555: LDA 6,-1(6)	# decrement end of stack pointer
556: LDA 4,1(4)	# increment offset
557: ADD 5,6,4	# set r5 back to next frame
558: ST 4,10(0)	# store offset in frame
559: LD 1,10(0)	# load right's temp value offset into r1
560: SUB 2,5,1	# get right value's address in DMEM
561: LD 1,0(3)	# load left operand value into r1
562: LD 2,0(2)	# load right operand value into r2
563: SUB 1,1,2	# subtract the two values
564: ST 1,-1(6)	# store difference into new temp value
565: LDA 6,-1(6)	# decrement end of stack pointer
566: SUB 4,5,6	# update current offset
567: ST 4,6(0)	# store offset in frame
568: LD 2,6(0)	# load arg1's offset into r2
569: SUB 3,5,2	# load temp arg1's address into r3
570: LD 2,0(3)	# load arg1 into r2
571: ST 2,-8(5)	# load arg1 into AR
572: LD 5,-6(5)	# set r5 to last frame to get variable den
573: LD 1,-9(5)	# load variable den into r1
574: ST 1,-1(6)	# store value into new temp variable
575: LDA 6,-1(6)	# decrement end of stack pointer
576: LDA 4,1(4)	# increment offset
577: ADD 5,6,4	# set r5 back to next frame
578: ST 4,7(0)	# store offset in frame
579: LD 2,7(0)	# load arg2's offset into r2
580: SUB 3,5,2	# load temp arg2's address into r3
581: LD 2,0(3)	# load arg2 into r2
582: ST 2,-9(5)	# load arg2 into AR
583: LDA 6,-9(5)	# reset end of frame to end of args
584: SUB 4,5,6	# update current offset
585: LDA 1,2(7)	# set r1 to return address
586: ST 1,-1(5)	# store return address into remainder's AR
587: LDA 7,501(0)	# jump to remainder
588: SUB 4,5,6	# update current offset
589: LD 1,-2(5)	# restore r1
590: LD 2,-3(5)	# restore r2
591: LD 3,-4(5)	# restore r3
592: LD 4,-5(5)	# restore r4
593: LD 6,-7(5)	# restore r6
594: LD 5,-6(5)	# restore r5
595: LDA 6,-1(6)	# decrement end of stack pointer
596: SUB 4,5,6	# update current offset
597: ST 4,5(0)	# store offset in frame
598: LD 1,5(0)	# load elseExpr's temp value offset into r1
599: SUB 3,5,1	# get temp value's address in DMEM
600: LD 2,0(3)	# load elseExpr value into r2
601: ST 2,-1(6)	# store value to new temp value
602: LDA 6,-1(6)	# decrement end of stack pointer
603: SUB 4,5,6	# update current offset
604: ST 4,0(0)	# store offset in frame
605: LD 1,0(6)	# load function's return value into r1
606: ST 1,0(5)	# put value from r1 into return value
607: LD 7,-1(5)	# load return address into r7
