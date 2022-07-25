;; Auto-generated. Do not edit!


(when (boundp 'ethercat_test::vel)
  (if (not (find-package "ETHERCAT_TEST"))
    (make-package "ETHERCAT_TEST"))
  (shadow 'vel (find-package "ETHERCAT_TEST")))
(unless (find-package "ETHERCAT_TEST::VEL")
  (make-package "ETHERCAT_TEST::VEL"))

(in-package "ROS")
;;//! \htmlinclude vel.msg.html


(defclass ethercat_test::vel
  :super ros::object
  :slots (_velocity ))

(defmethod ethercat_test::vel
  (:init
   (&key
    ((:velocity __velocity) (make-array 4 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _velocity __velocity)
   self)
  (:velocity
   (&optional __velocity)
   (if __velocity (setq _velocity __velocity)) _velocity)
  (:serialization-length
   ()
   (+
    ;; int32[4] _velocity
    (* 4    4)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[4] _velocity
     (dotimes (i 4)
       (write-long (elt _velocity i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[4] _velocity
   (dotimes (i (length _velocity))
     (setf (elt _velocity i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     )
   ;;
   self)
  )

(setf (get ethercat_test::vel :md5sum-) "f8dbe9fe5f891a8fdba5d30d5afaa9f6")
(setf (get ethercat_test::vel :datatype-) "ethercat_test/vel")
(setf (get ethercat_test::vel :definition-)
      "int32[4] velocity
")



(provide :ethercat_test/vel "f8dbe9fe5f891a8fdba5d30d5afaa9f6")


