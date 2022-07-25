;; Auto-generated. Do not edit!


(when (boundp 'ethercat_test::trajectory)
  (if (not (find-package "ETHERCAT_TEST"))
    (make-package "ETHERCAT_TEST"))
  (shadow 'trajectory (find-package "ETHERCAT_TEST")))
(unless (find-package "ETHERCAT_TEST::TRAJECTORY")
  (make-package "ETHERCAT_TEST::TRAJECTORY"))

(in-package "ROS")
;;//! \htmlinclude trajectory.msg.html


(defclass ethercat_test::trajectory
  :super ros::object
  :slots (_traj ))

(defmethod ethercat_test::trajectory
  (:init
   (&key
    ((:traj __traj) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _traj __traj)
   self)
  (:traj
   (&optional __traj)
   (if __traj (setq _traj __traj)) _traj)
  (:serialization-length
   ()
   (+
    ;; float64[] _traj
    (* 8    (length _traj)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _traj
     (write-long (length _traj) s)
     (dotimes (i (length _traj))
       (sys::poke (elt _traj i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _traj
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _traj (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _traj i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get ethercat_test::trajectory :md5sum-) "2c706e3135da03d0b3079ab165a03313")
(setf (get ethercat_test::trajectory :datatype-) "ethercat_test/trajectory")
(setf (get ethercat_test::trajectory :definition-)
      "float64[] traj

")



(provide :ethercat_test/trajectory "2c706e3135da03d0b3079ab165a03313")


