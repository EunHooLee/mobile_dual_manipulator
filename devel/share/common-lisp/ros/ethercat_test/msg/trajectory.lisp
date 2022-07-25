; Auto-generated. Do not edit!


(cl:in-package ethercat_test-msg)


;//! \htmlinclude trajectory.msg.html

(cl:defclass <trajectory> (roslisp-msg-protocol:ros-message)
  ((traj
    :reader traj
    :initarg :traj
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass trajectory (<trajectory>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <trajectory>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'trajectory)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ethercat_test-msg:<trajectory> is deprecated: use ethercat_test-msg:trajectory instead.")))

(cl:ensure-generic-function 'traj-val :lambda-list '(m))
(cl:defmethod traj-val ((m <trajectory>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ethercat_test-msg:traj-val is deprecated.  Use ethercat_test-msg:traj instead.")
  (traj m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <trajectory>) ostream)
  "Serializes a message object of type '<trajectory>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'traj))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'traj))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <trajectory>) istream)
  "Deserializes a message object of type '<trajectory>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'traj) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'traj)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<trajectory>)))
  "Returns string type for a message object of type '<trajectory>"
  "ethercat_test/trajectory")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'trajectory)))
  "Returns string type for a message object of type 'trajectory"
  "ethercat_test/trajectory")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<trajectory>)))
  "Returns md5sum for a message object of type '<trajectory>"
  "2c706e3135da03d0b3079ab165a03313")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'trajectory)))
  "Returns md5sum for a message object of type 'trajectory"
  "2c706e3135da03d0b3079ab165a03313")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<trajectory>)))
  "Returns full string definition for message of type '<trajectory>"
  (cl:format cl:nil "float64[] traj~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'trajectory)))
  "Returns full string definition for message of type 'trajectory"
  (cl:format cl:nil "float64[] traj~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <trajectory>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'traj) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <trajectory>))
  "Converts a ROS message object to a list"
  (cl:list 'trajectory
    (cl:cons ':traj (traj msg))
))
