 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        style = {'description_width': '250px'}
        layout = {'width': '400px'}

        self.persistence_time = FloatText(
          description='persistence_time',
          value=20,
          step=1,
          style=style, layout=layout)

        self.migration_speed = FloatText(
          description='migration_speed',
          value=2,
          step=0.1,
          style=style, layout=layout)

        self.migration_bias = FloatText(
          description='migration_bias',
          value=0.6,
          step=0.1,
          style=style, layout=layout)

        self.fixed_persistence = Checkbox(
          description='fixed_persistence',
          value=false,
          style=style, layout=layout)

        self.tracer_secretion = FloatText(
          description='tracer_secretion',
          value=1,
          step=0.1,
          style=style, layout=layout)

        self.number_of_cells = IntText(
          description='number_of_cells',
          value=3,
          step=0.1,
          style=style, layout=layout)

        param_button_layout={'width':'400px'} 

        desc_row1 = Button(description='mean persistence time', disabled=True, layout=param_button_layout) 
        desc_row1.style.button_color = 'lightgreen'
        desc_row2 = Button(description='migration speed', disabled=True, layout=param_button_layout) 
        desc_row2.style.button_color = 'tan'
        desc_row3 = Button(description='migration bias parameter', disabled=True, layout=param_button_layout) 
        desc_row3.style.button_color = 'lightgreen'
        desc_row4 = Button(description='true if each migration path has same duration (future PhysiCell versions)', disabled=True, layout=param_button_layout) 
        desc_row4.style.button_color = 'tan'
        desc_row5 = Button(description='how fast tracer is released', disabled=True, layout=param_button_layout) 
        desc_row5.style.button_color = 'lightgreen'
        desc_row6 = Button(description='number of cell tracks to simulate', disabled=True, layout=param_button_layout) 
        desc_row6.style.button_color = 'tan'

        row1 = [self.persistence_time, Label('min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row1] 
        row2 = [self.migration_speed, Label('micron/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row2] 
        row3 = [self.migration_bias, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row3] 
        row4 = [self.fixed_persistence, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row4] 
        row5 = [self.tracer_secretion, Label('1/min' , layout=Layout(flex='1 1 auto', width='auto')), desc_row5] 
        row6 = [self.number_of_cells, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row6] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.persistence_time.value = float(uep.find('.//persistence_time').text)
        self.migration_speed.value = float(uep.find('.//migration_speed').text)
        self.migration_bias.value = float(uep.find('.//migration_bias').text)
        self.fixed_persistence.value = bool(uep.find('.//fixed_persistence').text)
        self.tracer_secretion.value = float(uep.find('.//tracer_secretion').text)
        self.number_of_cells.value = int(uep.find('.//number_of_cells').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//persistence_time').text = str(self.persistence_time.value)
        uep.find('.//migration_speed').text = str(self.migration_speed.value)
        uep.find('.//migration_bias').text = str(self.migration_bias.value)
        uep.find('.//fixed_persistence').text = str(self.fixed_persistence.value)
        uep.find('.//tracer_secretion').text = str(self.tracer_secretion.value)
        uep.find('.//number_of_cells').text = str(self.number_of_cells.value)
