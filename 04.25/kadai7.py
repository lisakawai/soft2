(defun sqrt-iter (guess x)
  (if (good-enough? guess x)
     guess
    (sqrt-iter (improve guess x) x)))
sqrt-iter
(defun good-enough? (guess x) (< (abs (- (improve guess x) guess)) 0.0001))
good-enough\?
(defun improve (guess x) (/ (+ guess (/ x guess)) 2 ))
improve
(defun my-sqrt (x) (sqrt-iter 1.0 x))
my-sqrt
(defun square (x) (* x x))
square
(my-sqrt 2)
1.4142156862745097
(my-sqrt 0.01)
0.10000052895642693 ;;after

0.10000052895642693 ;;before
(my-sqrt 0.0001)
0.010000714038711746 ;;after
0.010000000025490743 ;;before
(my-sqrt 4)
2.0000000929222947
