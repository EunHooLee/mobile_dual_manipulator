;; Auto-generated. Do not edit!


(when (boundp 'mservo_msg::traj_1d)
  (if (not (find-package "MSERVO_MSG"))
    (make-package "MSERVO_MSG"))
  (shadow 'traj_1d (find-package "MSERVO_MSG")))
(unless (find-package "MSERVO_MSG::TRAJ_1D")
  (make-package "MSERVO_MSG::TRAJ_1D"))

(in-package "ROS")
;;//! \htmlinclude traj_1d.msg.html


(defclass mservo_msg::traj_1d
  :super ros::object
  :slots (_traj ))

(defmethod mservo_msg::traj_1d
  (:init
   (&key
    ((:traj __traj) (make-array 7 :initial-element 0.0 :element-type :float))
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
    ;; float64[7] _traj
    (* 8    7)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[7] _traj
     (dotimes (i 7)
       (sys::poke (elt _traj i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[7] _traj
   (dotimes (i (length _traj))
     (setf (elt _traj i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(setf (get mservo_msg::traj_1d :md5sum-) "58e9b5284e3c4cd3c99f99337b97f52c")
(setf (get mservo_msg::traj_1d :datatype-) "mservo_msg/traj_1d")
(setf (get mservo_msg::traj_1d :definition-)
      "float64[7] traj

")



(provide :mservo_msg/traj_1d "58e9b5284e3c4cd3c99f99337b97f52c")


