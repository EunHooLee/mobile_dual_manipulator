;; Auto-generated. Do not edit!


(when (boundp 'mservo_msg::traj_2d)
  (if (not (find-package "MSERVO_MSG"))
    (make-package "MSERVO_MSG"))
  (shadow 'traj_2d (find-package "MSERVO_MSG")))
(unless (find-package "MSERVO_MSG::TRAJ_2D")
  (make-package "MSERVO_MSG::TRAJ_2D"))

(in-package "ROS")
;;//! \htmlinclude traj_2d.msg.html


(defclass mservo_msg::traj_2d
  :super ros::object
  :slots (_traj_2d ))

(defmethod mservo_msg::traj_2d
  (:init
   (&key
    ((:traj_2d __traj_2d) (let (r) (dotimes (i 50) (push (instance mservo_msg::traj_1d :init) r)) r))
    )
   (send-super :init)
   (setq _traj_2d __traj_2d)
   self)
  (:traj_2d
   (&rest __traj_2d)
   (if (keywordp (car __traj_2d))
       (send* _traj_2d __traj_2d)
     (progn
       (if __traj_2d (setq _traj_2d (car __traj_2d)))
       _traj_2d)))
  (:serialization-length
   ()
   (+
    ;; mservo_msg/traj_1d[50] _traj_2d
    (apply #'+ (send-all _traj_2d :serialization-length))
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; mservo_msg/traj_1d[50] _traj_2d
     (dolist (elem _traj_2d)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; mservo_msg/traj_1d[50] _traj_2d
   (dotimes (i 50)
     (send (elt _traj_2d i) :deserialize buf ptr-) (incf ptr- (send (elt _traj_2d i) :serialization-length))
     )
   ;;
   self)
  )

(setf (get mservo_msg::traj_2d :md5sum-) "1e758c7f7f248e577c2b0cf954d10ea6")
(setf (get mservo_msg::traj_2d :datatype-) "mservo_msg/traj_2d")
(setf (get mservo_msg::traj_2d :definition-)
      "traj_1d[50] traj_2d

================================================================================
MSG: mservo_msg/traj_1d
float64[7] traj

")



(provide :mservo_msg/traj_2d "1e758c7f7f248e577c2b0cf954d10ea6")


