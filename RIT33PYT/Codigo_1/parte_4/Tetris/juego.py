#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Un Tetris con Pygame.
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


import random
import time
import pygame
import sys
from pygame.locals import *

from constantes import *

class Juego:
	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(TAMANIO_VENTANA)
		self.fonts = {
			'defaut': pygame.font.Font('freesansbold.ttf', 18),
			'titulo': pygame.font.Font('freesansbold.ttf', 100),
		}
		pygame.display.set_caption('Aplicación Tetris')
	def start(self):
		self._verTexto('Tetris', CENTRO_VENTANA, font='titulo')
		self._verTexto('Pulsar una tecla...', POS)
		self._espera()
	def stop(self):
		self._verTexto('Perdido', CENTRO_VENTANA, font='titulo')
		self._espera()
		self._salir()
	def _verTexto(self, text, posicion, colores=9, font='defaut'):
#		print("Ver Texto")
		font = self.fonts.get(font, self.fonts['defaut'])
		colores = COLORES.get(colores, COLORES[9])
		pintar = font.render(text, True, colores)
		rect = pintar.get_rect()
		rect.center = posicion
		self.surface.blit(pintar, rect)
	def _getEvent(self):
		for event in pygame.event.get():
			if event.type == SALIR:
				self._salir()
			if event.type == KEYUP:
				if event.key == K_ESCAPE:
					self._salir()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					continue
				return event.key
	def _salir(self):
		print("Salir")
		pygame.quit()
		sys.exit()
	def _pintar(self):
		pygame.display.update()
		self.clock.tick()
	def _espera(self):
		print("Espera")
		while self._getEvent() == None:
			self._pintar()
	def _getPieza(self):
		return PIEZAS.get(random.choice(PIEZAS_KEYS))
	def _getCurrentColorPieza(self):
		for l in self.current[0]:
			for c in l:
				if c != 0:
					return c
		return 0
	def _calcularDatosPiezaActual(self):
		m=self.current[self.posicion[2]]
		coords = []
		for i, l in enumerate(m):
			for j, k in enumerate(l):
				if k != 0:
					coords.append([i+self.posicion[0], j+self.posicion[1]])
		self.coordenadas = coords
	def _esValido(self, x=0, y=0, r=0):
		max_x, max_y = DIM_TABLERO
		if r == 0:
			coordenadas = self.coordenadas
		else:
			m=self.current[(self.posicion[2]+r)%len(self.current)]
			coords = []
			for i, l in enumerate(m):
				for j, k in enumerate(l):
					if k != 0:
						coords.append([i+self.posicion[0], j+self.posicion[1]])
			coordenadas = coords
#			print("Rotación verificada: %s" % coordenadas)
		for cx, cy in coordenadas:
			if not 0 <= x + cx < max_x:
#				print("No válido en X: cx=%s, x=%s" % (cx, x))
				return False
			elif cy <0:
				continue
			elif y + cy >= max_y:
#				print("No válido en Y: cy=%s, y=%s" % (cy, y))
				return False
			else:
				if self.tablero[cy+y][cx+x] != 0:
#					print("Posición ocupada en el tablero")
					return False
#		print("Posición verificada válida: x=%s, y=%s" % (x, y))
		return True
	def _posarPieza(self):
		print("La pieza se ha posado")
		if self.posicion[1] <= 0:
			self.perdido = True
		# Agregar la pieza entre el tablero
		colores = self._getCurrentColorPieza()
		for cx, cy in self.coordenadas:
			self.tablero[cy][cx] = colores
		completas = []
		# calcular las líneas completas
		for i, line in enumerate(self.tablero[::-1]):
			for casilla in line:
				if casilla == 0:
					break
			else:
				print(self.tablero)
				print(">>> %s" % (DIM_TABLERO[1]-1-i))
				completas.append(DIM_TABLERO[1]-1-i)
		lineas = len(completas)
		for i in completas:
			self.tablero.pop(i)
		for i in range(lineas):
			self.tablero.insert(0, [0] * DIM_TABLERO[0])
		# calcular el score y otro
		self.lineas += lineas
		self.score += lineas * self.nivel
		self.nivel = int(self.lineas / 10) + 1
		if lineas >= 4:
			self.tetris +=1
			self.score += self.nivel * self.tetris
		# Trabajo con la pieza actual terminada
		self.current = None
	def _first(self):
		self.tablero = [[0] * DIM_TABLERO[0] for i in range(DIM_TABLERO[1])]
		self.score, self.piezas, self.lineas, self.tetris, self.nivel = 0, 0, 0, 0, 1
		self.current, self.next, self.perdido = None, self._getPieza(), False
	def _next(self):
		print("Pieza siguiente")
		self.current, self.next = self.next, self._getPieza()
		self.piezas += 1
		self.posicion = [int(DIM_TABLERO[0] / 2)-2, -4, 0]
		self._calcularDatosPiezaActual()
		self.ultimo_movimiento = self.ultimo_caida = time.time()
	def _administrarEventos(self):
		event = self._getEvent()
		if event == K_p:
			print("Pausa")
			self.surface.fill(COLORES.get(0))
			self._verTexto('Pausa', CENTRO_VENTANA, font='titulo')
			self._verTexto('Pulsar una tecla...', POS)
			self._espera()
		elif event == K_LEFT:
			print("Movimiento a la izquierda")
			if self._esValido(x=-1):
				self.posicion[0] -= 1
		elif event == K_RIGHT:
			print("Movimiento a la derecha")
			if self._esValido(x=1):
				self.posicion[0] += 1
		elif event == K_DOWN:
			print("Movimiento hacia abajo")
			if self._esValido(y=1):
				self.posicion[1] += 1
		elif event == K_UP:
			print("Movimiento de rotacion")
			if self._esValido(r=1):
				self.posicion[2] = (self.posicion[2] + 1) %len(self.current)
		elif event == K_SPACE:
			print("Movimiento de caída %s / %s" % (self.posicion, self.coordenadas))
			if self.posicion[1] <=0:
				self.posicion[1] = 1
				self._calcularDatosPiezaActual()
			a = 0
			while self._esValido(y=a):
				a+=1
			self.posicion[1] += a-1
		self._calcularDatosPiezaActual()
	def _administrarGravedad(self):
		if time.time() - self.ultimo_caida > GRAVEDAD:
			self.ultimo_caida = time.time()
			if not self._esValido():
				print ("Estamos en una posición inválida")
				self.posicion[1] -= 1
				self._calcularDatosPiezaActual()
				self._posarPieza()
			elif self._esValido() and not self._esValido(y=1):
				self._calcularDatosPiezaActual()
				self._posarPieza()
			else:
				print("Nos movemos hacia abajo")
				self.posicion[1] += 1
				self._calcularDatosPiezaActual()
	def _diseniarTablero(self):
		self.surface.fill(COLORES.get(0))
		pygame.draw.rect(self.surface, COLORES[8], START_ESCENA+TAMANIO_ESCENA, BORDE_TABLERO)
		for i, linea in enumerate(self.tablero):
			for j, casilla in enumerate(linea):
				colores = COLORES[casilla]
				posicion = j, i
				coordenadas = tuple([START_TABLERO[k] + posicion[k] * TAMANIO_BLOQUE[k] for k in range(2)])
				pygame.draw.rect(self.surface, colores, coordenadas + TAMANIO_BLOQUE)
		if self.current is not None:
			for posicion in self.coordenadas:
				colores = COLORES.get(self._getCurrentColorPieza())
				coordenadas = tuple([START_TABLERO[k] + posicion[k] * TAMANIO_BLOQUE[k] for k in range(2)])
				pygame.draw.rect(self.surface, colores, coordenadas + TAMANIO_BLOQUE)
		self.score, self.piezas, self.lineas, self.tetris, self.nivel#TODO
		self._verTexto('Score: >%s' % self.score, POSICION_SCORE)
		self._verTexto('Piezas: %s' % self.piezas, POSICION_PIEZAS)
		self._verTexto('Líneas: %s' % self.lineas, POSICION_LINEAS)
		self._verTexto('Tetris: %s' % self.tetris, POSICION_TETRIS)
		self._verTexto('Nivel: %s' % self.nivel, POSICION_NIVEL)

		self._pintar()
	def play(self):
		print("Jugar")
		self.surface.fill(COLORES.get(0))
		self._first()
		while not self.perdido:
			if self.current is None:
				self._next()
			self._administrarEventos()
			self._administrarGravedad()
			self._diseniarTablero()

if __name__ == '__main__':
	j = Juego()
	print("Juego listo")
	j.start()
	print("Partida iniciada")
	j.play()
	print("Partida terminada")
	j.stop()
	print("Parada del programa")

