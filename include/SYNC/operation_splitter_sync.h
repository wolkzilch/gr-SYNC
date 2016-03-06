/* -*- c++ -*- */
/* 
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_SYNC_OPERATION_SPLITTER_SYNC_H
#define INCLUDED_SYNC_OPERATION_SPLITTER_SYNC_H

#include <SYNC/api.h>
#include <gnuradio/sync_decimator.h>

namespace gr {
  namespace SYNC {

    /*!
     * \brief <+description of block+>
     * \ingroup SYNC
     *
     */
    class SYNC_API operation_splitter_sync : virtual public gr::sync_decimator
    {
     public:
      typedef boost::shared_ptr<operation_splitter_sync> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of SYNC::operation_splitter_sync.
       *
       * To avoid accidental use of raw pointers, SYNC::operation_splitter_sync's
       * constructor is in a private implementation
       * class. SYNC::operation_splitter_sync::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace SYNC
} // namespace gr

#endif /* INCLUDED_SYNC_OPERATION_SPLITTER_SYNC_H */

