;; Auto-generated. Do not edit!


(when (boundp 'dxl_gripper::GripperDist)
  (if (not (find-package "DXL_GRIPPER"))
    (make-package "DXL_GRIPPER"))
  (shadow 'GripperDist (find-package "DXL_GRIPPER")))
(unless (find-package "DXL_GRIPPER::GRIPPERDIST")
  (make-package "DXL_GRIPPER::GRIPPERDIST"))
(unless (find-package "DXL_GRIPPER::GRIPPERDISTREQUEST")
  (make-package "DXL_GRIPPER::GRIPPERDISTREQUEST"))
(unless (find-package "DXL_GRIPPER::GRIPPERDISTRESPONSE")
  (make-package "DXL_GRIPPER::GRIPPERDISTRESPONSE"))

(in-package "ROS")





(defclass dxl_gripper::GripperDistRequest
  :super ros::object
  :slots (_dist ))

(defmethod dxl_gripper::GripperDistRequest
  (:init
   (&key
    ((:dist __dist) 0.0)
    )
   (send-super :init)
   (setq _dist (float __dist))
   self)
  (:dist
   (&optional __dist)
   (if __dist (setq _dist __dist)) _dist)
  (:serialization-length
   ()
   (+
    ;; float32 _dist
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _dist
       (sys::poke _dist (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _dist
     (setq _dist (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass dxl_gripper::GripperDistResponse
  :super ros::object
  :slots (_result ))

(defmethod dxl_gripper::GripperDistResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional (__result :null))
   (if (not (eq __result :null)) (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass dxl_gripper::GripperDist
  :super ros::object
  :slots ())

(setf (get dxl_gripper::GripperDist :md5sum-) "47ad84b25c08b18a1fb3684555468caf")
(setf (get dxl_gripper::GripperDist :datatype-) "dxl_gripper/GripperDist")
(setf (get dxl_gripper::GripperDist :request) dxl_gripper::GripperDistRequest)
(setf (get dxl_gripper::GripperDist :response) dxl_gripper::GripperDistResponse)

(defmethod dxl_gripper::GripperDistRequest
  (:response () (instance dxl_gripper::GripperDistResponse :init)))

(setf (get dxl_gripper::GripperDistRequest :md5sum-) "47ad84b25c08b18a1fb3684555468caf")
(setf (get dxl_gripper::GripperDistRequest :datatype-) "dxl_gripper/GripperDistRequest")
(setf (get dxl_gripper::GripperDistRequest :definition-)
      "float32 dist
---
bool result

")

(setf (get dxl_gripper::GripperDistResponse :md5sum-) "47ad84b25c08b18a1fb3684555468caf")
(setf (get dxl_gripper::GripperDistResponse :datatype-) "dxl_gripper/GripperDistResponse")
(setf (get dxl_gripper::GripperDistResponse :definition-)
      "float32 dist
---
bool result

")



(provide :dxl_gripper/GripperDist "47ad84b25c08b18a1fb3684555468caf")


