(define (problem BLOCKS-14-0)
(:domain ma-blocksworld)
(:objects
 r0 r1 r2 r3 - robot
 k a f l d b m e j n h i c g - block
)
(:shared-data
  ((on ?b - block) - block)
  (ontable ?b - block)
  (clear ?b - block)
  ((holding ?r - robot) - block) - 
(either r0 r1 r2)
)
(:init
 (myAgent r3)
 (= (holding r0) nob)
 (= (holding r1) nob)
 (= (holding r2) nob)
 (= (holding r3) nob)
 (not (clear k))
 (= (on k) c)
 (not (ontable k))
 (clear a)
 (= (on a) j)
 (not (ontable a))
 (clear f)
 (ontable f)
 (= (on f) nob)
 (not (clear l))
 (= (on l) b)
 (not (ontable l))
 (not (clear d))
 (= (on d) i)
 (not (ontable d))
 (not (clear b))
 (= (on b) e)
 (not (ontable b))
 (not (clear m))
 (= (on m) k)
 (not (ontable m))
 (not (clear e))
 (ontable e)
 (= (on e) nob)
 (not (clear j))
 (= (on j) h)
 (not (ontable j))
 (not (clear n))
 (ontable n)
 (= (on n) nob)
 (not (clear h))
 (= (on h) m)
 (not (ontable h))
 (not (clear i))
 (= (on i) n)
 (not (ontable i))
 (not (clear c))
 (= (on c) l)
 (not (ontable c))
 (clear g)
 (= (on g) d)
 (not (ontable g))
)
(:global-goal (and
 (= (on e) l)
 (= (on l) f)
 (= (on f) b)
 (= (on b) j)
 (= (on j) i)
 (= (on i) n)
 (= (on n) c)
 (= (on c) k)
 (= (on k) g)
 (= (on g) d)
 (= (on d) m)
 (= (on m) a)
 (= (on a) h)
)))