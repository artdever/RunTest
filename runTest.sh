#!/bin/bash
echo "$(cat <<EOF
DATE: 04/05/2024
Hostname: myhost

7 tests will be run:
test1
test2
test3
test4
test5
test6
test7
Running test1 ... Completed FAIL [Performance]
Running test2 ... Completed FAIL [Crash]
Running test3 ... Completed PASS
Running test4 ... Completed FAIL [Expected fail]
Running test5 ... Completed FAIL [Expected fail]
Running test6 ... Completed FAIL [Crash]
Running test7 ... Completed PASS
--------------------------
FAILED – 5
test1 [Performance]
test2 [Crash]
test4 [Expected fail]
test5 [Expected fail]
test6 [Crash]

TOTAL RUNTIME: 234

REGRESSION PASS RATE: 5/7
OVERALL STATUS: FAILED
DATE: 04/05/2024
Hostname: myhost

7 tests will be run:
test1
test2
test3
test4
test5
test6
test7
Running test1 ... Completed PASS
Running test2 ... Completed FAIL [Crash]
Running test3 ... Completed FAIL [Performance]
Running test4 ... Completed FAIL [Expected fail]
Running test5 ... Completed FAIL [Expected fail]
Running test6 ... Completed PASS
Running test7 ... Completed PASS
--------------------------
FAILED – 4
test2 [Crash]
test3 [Performance]
test4 [Expected fail]
test5 [Expected fail]

TOTAL RUNTIME: 234

REGRESSION PASS RATE: 4/7
OVERALL STATUS: FAILED
DATE: 04/05/2024
Hostname: myhost

7 tests will be run:
test1
test2
test3
test4
test5
test6
test7
Running test1 ... Completed FAIL [Performance]
Running test2 ... Completed FAIL [Crash]
Running test3 ... Completed PASS
Running test4 ... Completed FAIL [Expected fail]
Running test5 ... Completed FAIL [Expected fail]
Running test6 ... Completed FAIL [Crash]
Running test7 ... Completed PASS
--------------------------
FAILED – 5
test1 [Performance]
test2 [Crash]
test4 [Expected fail]
test5 [Expected fail]
test6 [Crash]

TOTAL RUNTIME: 234

REGRESSION PASS RATE: 5/7
OVERALL STATUS: FAILED

Running test1 ... Completed FAIL [Performance]
Running test2 ... Completed FAIL [Crash]
Running test3 ... Completed PASS
Running test4 ... Completed FAIL [Expected fail]
Running test5 ... Completed FAIL [Expected fail]
Running test6 ... Completed FAIL [Crash]
Running test7 ... Completed PASS
--------------------------
FAILED – 5
test1 [Performance]
test2 [Crash]
test4 [Expected fail]
test5 [Expected fail]
test6 [Crash]

TOTAL RUNTIME: 234

REGRESSION PASS RATE: 5/7
OVERALL STATUS: FAILED
DATE: 04/05/2024
Hostname: myhost

7 tests will be run:
test1
test2
test3
test4
test5
test6
test7
Running test1 ... Completed PASS
Running test2 ... Completed FAIL [Crash]
Running test3 ... Completed PASS
Running test4 ... Completed FAIL [Expected fail]
Running test5 ... Completed FAIL [Expected fail]
Running test6 ... Completed PASS
Running test7 ... Completed PASS
--------------------------
FAILED – 3
test2 [Crash]
test4 [Expected fail]
test5 [Expected fail]

TOTAL RUNTIME: 234

REGRESSION PASS RATE: 3/7
OVERALL STATUS: FAILED
EOF
)"
