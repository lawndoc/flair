0: LD 5,0(0)	# set r5 to bottom of dmem
1: LDA 6,-7,5	# set r6 to end of RunSum's AR
2: SUB 4,5,6	# update current offset
3: LD 2,1(0)	# load arg1 into r2
4: ST 2,-8(5)	# load arg1 into AR
5: LDA 6,-1(6)	# decrement end of stack pointer
6: SUB 4,5,6	# update current offset
7: LDA 1,5(7)	# set r1 to return address
8: ST 1,-1(5)	# store return address into RunSum's AR
9: ST 6,-7(5)	# save register 6 to AR
10: ST 5,-6(5)	# save register 5 to AR
11: ST 4,-5(5)	# save register 4 to AR
12: LDA 7,28(0)	# jump to RunSum
13: LD 1,-2(5)	# restore r1
14: LD 2,-3(5)	# restore r2
15: LD 3,-4(5)	# restore r3
16: LD 4,-5(5)	# restore r4
17: LD 6,-7(5)	# restore r6
18: LD 5,-6(5)	# restore r5
19: LD 2,0(5)	# put return value from RunSum into r2
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
* RunSum
*
28: ST 6,-8(6)	# save register 6 to AR
29: ST 5,-7(6)	# save register 5 to AR
30: ST 4,-6(6)	# save register 4 to AR
31: ST 3,-5(6)	# save register 3 to AR
32: ST 2,-4(6)	# save register 2 to AR
33: ST 1,-3(6)	# save register 1 to AR
34: LDA 5,-1(6)	# set r5 to beginning of recursiveAdd's AR
35: LDA 6,-7,5	# set r6 to end of recursiveAdd's AR
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
48: LDA 6,-8(5)	# reset end of frame to end of args
49: SUB 4,5,6	# update current offset
50: LDA 1,2(7)	# set r1 to return address
51: ST 1,-1(5)	# store return address into recursiveAdd's AR
52: LDA 7,66(0)	# jump to recursiveAdd
53: SUB 4,5,6	# update current offset
54: LD 1,-2(5)	# restore r1
55: LD 2,-3(5)	# restore r2
56: LD 3,-4(5)	# restore r3
57: LD 4,-5(5)	# restore r4
58: LD 6,-7(5)	# restore r6
59: LD 5,-6(5)	# restore r5
60: LDA 6,-1(6)	# decrement end of stack pointer
61: SUB 4,5,6	# update current offset
62: ST 4,0(0)	# store offset in frame
63: LD 1,0(6)	# load function's return value into r1
64: ST 1,0(5)	# put value from r1 into return value
65: LD 7,-1(5)	# load return address into r7
*
* recursiveAdd
*
66: LDC 1,8(0)	# load arg slot into r1
67: ST 1,6(0)	# store offset in frame
68: LD 1,6(0)	# load left's temp value offset into r1
69: SUB 3,5,1	# get left value's address in DMEM
70: LDC 1,1(0)	# load 1 into r1
71: ST 1,-1(6)	# copy r1 into new temp value
72: LDA 6,-1(6)	# decrement end of stack pointer
73: SUB 4,5,6	# update current offset
74: ST 4,7(0)	# store offset in frame
75: LD 1,7(0)	# load right's temp value offset into r1
76: SUB 2,5,1	# get right value's address in DMEM
77: LD 1,0(3)	# load left operand value into r1
78: LD 2,0(2)	# load right operand value into r2
79: SUB 1,1,2	# subtract right operand from the left
80: JEQ 1,2(7)	# jump if left equals right
81: ST 0,-1(6)	# load false into new temp var
82: LDA 7,2(7)	# skip not equal
83: LDC 1,1(0)	# load 1 (true) into r1
84: ST 1,-1(6)	# load true into new temp var
85: LDA 6,-1(6)	# decrement end of stack pointer
86: SUB 4,5,6	# update current offset
87: ST 4,3(0)	# store offset in frame
88: LD 1,3(0)	# load ifExpr's temp value offset into r1
89: SUB 3,5,1	# get temp value's address in DMEM
90: LD 1,0(3)	# load ifExpr value into r1
91: JEQ 1,1(7)	# jump to else clause if false
92: LDA 7,2(7)	# jump to then clause
93: LDC 1,102(0)	# load else clause address
94: LDA 7,0(1)	# jump to else clause
95: LDC 1,8(0)	# load arg slot into r1
96: ST 1,4(0)	# store offset in frame
97: LD 1,4(0)	# load thenExpr's temp value offset into r1
98: SUB 3,5,1	# get temp value's address in DMEM
99: LD 2,0(3)	# load thenExpr value into r2
100: LDC 1,169(0)	# load end if address
101: LDA 7,0(1)	# jump over else clause to end if
102: LDC 1,8(0)	# load arg slot into r1
103: ST 1,6(0)	# store offset in frame
104: LD 1,6(0)	# load left's temp value offset into r1
105: SUB 3,5,1	# get left value's address in DMEM
106: ST 6,-8(6)	# save register 6 to AR
107: ST 5,-7(6)	# save register 5 to AR
108: ST 4,-6(6)	# save register 4 to AR
109: ST 3,-5(6)	# save register 3 to AR
110: ST 2,-4(6)	# save register 2 to AR
111: ST 1,-3(6)	# save register 1 to AR
112: LDA 5,-1(6)	# set r5 to beginning of recursiveAdd's AR
113: LDA 6,-7,5	# set r6 to end of recursiveAdd's AR
114: SUB 4,5,6	# update current offset
115: LD 5,-6(5)	# set r5 to last frame to get variable n
116: LD 1,-8(5)	# load variable n into r1
117: ST 1,-1(6)	# store value into new temp variable
118: LDA 6,-1(6)	# decrement end of stack pointer
119: LDA 4,1(4)	# increment offset
120: ADD 5,6,4	# set r5 back to next frame
121: ST 4,12(0)	# store offset in frame
122: LD 1,12(0)	# load left's temp value offset into r1
123: SUB 3,5,1	# get left value's address in DMEM
124: LDC 1,1(0)	# load 1 into r1
125: ST 1,-1(6)	# copy r1 into new temp value
126: LDA 6,-1(6)	# decrement end of stack pointer
127: SUB 4,5,6	# update current offset
128: ST 4,13(0)	# store offset in frame
129: LD 1,13(0)	# load right's temp value offset into r1
130: SUB 2,5,1	# get right value's address in DMEM
131: LD 1,0(3)	# load left operand value into r1
132: LD 2,0(2)	# load right operand value into r2
133: SUB 1,1,2	# subtract the two values
134: ST 1,-1(6)	# store difference into new temp value
135: LDA 6,-1(6)	# decrement end of stack pointer
136: SUB 4,5,6	# update current offset
137: ST 4,9(0)	# store offset in frame
138: LD 2,9(0)	# load arg1's offset into r2
139: SUB 3,5,2	# load temp arg1's address into r3
140: LD 2,0(3)	# load arg1 into r2
141: ST 2,-8(5)	# load arg1 into AR
142: LDA 6,-8(5)	# reset end of frame to end of args
143: SUB 4,5,6	# update current offset
144: LDA 1,2(7)	# set r1 to return address
145: ST 1,-1(5)	# store return address into recursiveAdd's AR
146: LDA 7,66(0)	# jump to recursiveAdd
147: SUB 4,5,6	# update current offset
148: LD 1,-2(5)	# restore r1
149: LD 2,-3(5)	# restore r2
150: LD 3,-4(5)	# restore r3
151: LD 4,-5(5)	# restore r4
152: LD 6,-7(5)	# restore r6
153: LD 5,-6(5)	# restore r5
154: LDA 6,-1(6)	# decrement end of stack pointer
155: SUB 4,5,6	# update current offset
156: ST 4,7(0)	# store offset in frame
157: LD 1,7(0)	# load right's temp value offset into r1
158: SUB 2,5,1	# get right value's address in DMEM
159: LD 1,0(3)	# load left operand value into r1
160: LD 2,0(2)	# load right operand value into r2
161: ADD 1,1,2	# add the two values
162: ST 1,-1(6)	# store sum into new temp value
163: LDA 6,-1(6)	# decrement end of stack pointer
164: SUB 4,5,6	# update current offset
165: ST 4,5(0)	# store offset in frame
166: LD 1,5(0)	# load elseExpr's temp value offset into r1
167: SUB 3,5,1	# get temp value's address in DMEM
168: LD 2,0(3)	# load elseExpr value into r2
169: ST 2,-1(6)	# store value to new temp value
170: LDA 6,-1(6)	# decrement end of stack pointer
171: SUB 4,5,6	# update current offset
172: ST 4,0(0)	# store offset in frame
173: LD 1,0(6)	# load function's return value into r1
174: ST 1,0(5)	# put value from r1 into return value
175: LD 7,-1(5)	# load return address into r7
