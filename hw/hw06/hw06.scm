;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond((> x 0)1)
  	((= x 0)0)
  	((< x 0)-1)
))

(define (square x) (* x x))

(define (pow b n)
	(cond( (zero? n) 1)
		(else (* b (pow b (- n 1))))))


(define (unique s)
  (if (null? s) nil
      (cons (car s)
            (unique (filter (lambda (x) (not (eq? (car s) x))) (cdr s)))))
)