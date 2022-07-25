;; Auto-generated. Do not edit!


(when (boundp 'mservo_msg::joint_queue)
  (if (not (find-package "MSERVO_MSG"))
    (make-package "MSERVO_MSG"))
  (shadow 'joint_queue (find-package "MSERVO_MSG")))
(unless (find-package "MSERVO_MSG::JOINT_QUEUE")
  (make-package "MSERVO_MSG::JOINT_QUEUE"))

(in-package "ROS")
;;//! \htmlinclude joint_queue.msg.html


(defclass mservo_msg::joint_queue
  :super ros::object
  :slots (_jointq ))

(defmethod mservo_msg::joint_queue
  (:init
   (&key
    ((:jointq __jointq) (let (r) (dotimes (i 2) (push (instance mservo_msg::joint_data :init) r)) r))
    )
   (send-super :init)
   (setq _jointq __jointq)
   self)
  (:jointq
   (&rest __jointq)
   (if (keywordp (car __jointq))
       (send* _jointq __jointq)
     (progn
       (if __jointq (setq _jointq (car __jointq)))
       _jointq)))
  (:serialization-length
   ()
   (+
    ;; mservo_msg/joint_data[2] _jointq
    (apply #'+ (send-all _jointq :serialization-length))
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; mservo_msg/joint_data[2] _jointq
     (dolist (elem _jointq)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; mservo_msg/joint_data[2] _jointq
   (dotimes (i 2)
     (send (elt _jointq i) :deserialize buf ptr-) (incf ptr- (send (elt _jointq i) :serialization-length))
     )
   ;;
   self)
  )

(setf (get mservo_msg::joint_queue :md5sum-) "975ac8b6c2831749c6d3e61906fa26d9")
(setf (get mservo_msg::joint_queue :datatype-) "mservo_msg/joint_queue")
(setf (get mservo_msg::joint_queue :definition-)
      "joint_data[2] jointq

================================================================================
MSG: mservo_msg/joint_data
int32[7] pos

")



(provide :mservo_msg/joint_queue "975ac8b6c2831749c6d3e61906fa26d9")


