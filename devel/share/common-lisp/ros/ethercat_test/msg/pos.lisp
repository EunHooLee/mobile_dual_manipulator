; Auto-generated. Do not edit!


(cl:in-package ethercat_test-msg)


;//! \htmlinclude pos.msg.html

(cl:defclass <pos> (roslisp-msg-protocol:ros-message)
  ((position
    :reader position
    :initarg :position
    :type (cl:vector cl:integer)
   :initform (cl:make-array 7 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass pos (<pos>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pos>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pos)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ethercat_test-msg:<pos> is deprecated: use ethercat_test-msg:pos instead.")))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <pos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ethercat_test-msg:position-val is deprecated.  Use ethercat_test-msg:position instead.")
  (position m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pos>) ostream)
  "Serializes a message object of type '<pos>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'position))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pos>) istream)
  "Deserializes a message object of type '<pos>"
  (cl:setf (cl:slot-value msg 'position) (cl:make-array 7))
  (cl:let ((vals (cl:slot-value msg 'position)))
    (cl:dotimes (i 7)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pos>)))
  "Returns string type for a message object of type '<pos>"
  "ethercat_test/pos")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pos)))
  "Returns string type for a message object of type 'pos"
  "ethercat_test/pos")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pos>)))
  "Returns md5sum for a message object of type '<pos>"
  "fa44e48694f6c8d9c41d364ed0879145")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pos)))
  "Returns md5sum for a message object of type 'pos"
  "fa44e48694f6c8d9c41d364ed0879145")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pos>)))
  "Returns full string definition for message of type '<pos>"
  (cl:format cl:nil "int32[7] position~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pos)))
  "Returns full string definition for message of type 'pos"
  (cl:format cl:nil "int32[7] position~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pos>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'position) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pos>))
  "Converts a ROS message object to a list"
  (cl:list 'pos
    (cl:cons ':position (position msg))
))
