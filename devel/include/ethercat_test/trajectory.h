// Generated by gencpp from file ethercat_test/trajectory.msg
// DO NOT EDIT!


#ifndef ETHERCAT_TEST_MESSAGE_TRAJECTORY_H
#define ETHERCAT_TEST_MESSAGE_TRAJECTORY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ethercat_test
{
template <class ContainerAllocator>
struct trajectory_
{
  typedef trajectory_<ContainerAllocator> Type;

  trajectory_()
    : traj()  {
    }
  trajectory_(const ContainerAllocator& _alloc)
    : traj(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _traj_type;
  _traj_type traj;





  typedef boost::shared_ptr< ::ethercat_test::trajectory_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ethercat_test::trajectory_<ContainerAllocator> const> ConstPtr;

}; // struct trajectory_

typedef ::ethercat_test::trajectory_<std::allocator<void> > trajectory;

typedef boost::shared_ptr< ::ethercat_test::trajectory > trajectoryPtr;
typedef boost::shared_ptr< ::ethercat_test::trajectory const> trajectoryConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ethercat_test::trajectory_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ethercat_test::trajectory_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ethercat_test::trajectory_<ContainerAllocator1> & lhs, const ::ethercat_test::trajectory_<ContainerAllocator2> & rhs)
{
  return lhs.traj == rhs.traj;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ethercat_test::trajectory_<ContainerAllocator1> & lhs, const ::ethercat_test::trajectory_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ethercat_test

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ethercat_test::trajectory_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ethercat_test::trajectory_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ethercat_test::trajectory_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ethercat_test::trajectory_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ethercat_test::trajectory_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ethercat_test::trajectory_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ethercat_test::trajectory_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2c706e3135da03d0b3079ab165a03313";
  }

  static const char* value(const ::ethercat_test::trajectory_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2c706e3135da03d0ULL;
  static const uint64_t static_value2 = 0xb3079ab165a03313ULL;
};

template<class ContainerAllocator>
struct DataType< ::ethercat_test::trajectory_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ethercat_test/trajectory";
  }

  static const char* value(const ::ethercat_test::trajectory_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ethercat_test::trajectory_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64[] traj\n"
;
  }

  static const char* value(const ::ethercat_test::trajectory_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ethercat_test::trajectory_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.traj);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct trajectory_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ethercat_test::trajectory_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ethercat_test::trajectory_<ContainerAllocator>& v)
  {
    s << indent << "traj[]" << std::endl;
    for (size_t i = 0; i < v.traj.size(); ++i)
    {
      s << indent << "  traj[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.traj[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ETHERCAT_TEST_MESSAGE_TRAJECTORY_H
