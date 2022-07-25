;; Auto-generated. Do not edit!


(when (boundp 'ethercat_test::pos)
  (if (not (find-package "ETHERCAT_TEST"))
    (make-package "ETHERCAT_TEST"))
  (shadow 'pos (find-package "ETHERCAT_TEST")))
(unless (find-package "ETHERCAT_TEST::POS")
  (make-package "ETHERCAT_TEST::POS"))

(in-package "ROS")
;;//! \htmlinclude pos.msg.html


(defclass ethercat_test::pos
  :super ros::object
  :slots (_position ))

(defmethod ethercat_test::pos
  (:init
   (&key
    ((:position __position) (make-array 7 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _position __position)
   self)
  (:position
   (&optional __position)
   (if __position (setq _position __position)) _position)
  (:serialization-length
   ()
   (+
    ;; int32[7] _position
    (* 4    7)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[7] _position
     (dotimes (i 7)
       (write-long (elt _position i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[7] _position
   (dotimes (i (length _position))
     (setf (elt _position i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     )
   ;;
   self)
  )

(setf (get ethercat_test::pos :md5sum-) "fa44e48694f6c8d9c41d364ed0879145")
(setf (get ethercat_test::pos :datatype-) "ethercat_test/pos")
(setf (get ethercat_test::pos :definition-)
      "int32[7] position

")



(provide :ethercat_test/pos "fa44e48694f6c8d9c41d364ed0879145")


