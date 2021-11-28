# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MachineLearningDeslizamientos
                                 A QGIS plugin
 Predice areas de deslizamiento 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-04-08
        copyright            : (C) 2021 by Aldo Diaz/ GCG
        email                : mecatronica.gcg@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MachineLearningDeslizamientos class from file MachineLearningDeslizamientos.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Machine_Learning_Deslizamientos import MachineLearningDeslizamientos
    return MachineLearningDeslizamientos(iface)