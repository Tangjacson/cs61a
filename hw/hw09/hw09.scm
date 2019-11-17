
; Tail recursion

(define (replicate x n)
  'YOUR-CODE-HERE
  )

(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
)

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  'YOUR-CODE-HERE
)


(define (nondecreastream s)
    'YOUR-CODE-HERE)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))