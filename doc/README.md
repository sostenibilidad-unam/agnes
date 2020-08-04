# Agency Network Serializer

## Introduction

Agency Network Analylses map the social action arena of people by
situating them relative to their collaborators and within their
problem space. This helps actors identify where they have agency in
the system, i.e. over what elements and through what relationships.

This mapping is done via a multi-part interview process during which
data is gathered about actors (their context, worplaces, type of
organization, etc.), their activities (practices, capacities), and
their relationships to other actors.

AgNeS is a database administration interface specifically designed to
easily and sistematically gather data for agency network analyses.
Once data is loaded into an ANA database, network structure metrics
can be computed, it can be visualized in several ways or exported to
common standard formats for further processing with other software.


## Database Architecture

Information is grouped into tables made up of rows and columns, so
that each row holds data from related items. For example a "People"
table has rows with columns such as "name" and "e-mail".

Links can be created that join different tables together. For example
the "People" table might be related to an "Organization" table whose
rows contain columns for names and addresses of different organizations.

Constraints can be set on each column, so that only valid data can be
entered. This helps keep data consistent.

The resulting structure can be interrogated with great flexibility,
for example one might ask for a list of all members of organizations
in a given city.

This architecture is implemented a specialized kind of software called
a relational database. On top of such a database, we have developed a
web application which allows users to acces tables from their web
browsers, through the internet.

The following subsections describe the makeup of each of the tables we
have designed.

Of special interest are the "Edge" tables, which hold relationships
among nodes in the networks that make up the Agency Network Analysis.

![table scheme](../tables.png)

### Data about people

 - Sector (academia, ngo, etc.)
 - Organization (government body, ) 
 - collaborators, relationships
 - practices-actions, capacities
	
### Data about the perception-understanding of a system 

 - Biophysical and socio-political variables

## Networks in an ANA
 
### Agency networks
	Visualizations
	 - hiveplot
	
### Social network (person, person)


### Power network (avatar, power)

 
### Cognitive maps (variable, variable)

They are abstractions or internal representations of how a system works.

Examples: 

a) Cognitive Map of an academic

Here a picture of a cognitive map of the perception of
management and state of a natural protected area of the university
(with socio-political & biophysical variables)

b) Agency Network of a Laboratory that studies the Natural Protected Area-NPA (5 egos, each with 3-4 alters)

Show a picture of how they look after a SSI - what data they show

Egos: 

 1. Dr. Nigel (anthropologist)
 2. MSc. Mischa (Lab Tech)
 3. Dr. Sandra (biologist)
 4. Ms. Mirna, (sustainability student)
 5. Mr. Jared (CEO of an environmental NGO)

Alters:

 EGO1: MSc. Mischa, Mr. Jared, Dr. Repsa (head of the NPA)
 EGO2: Dr. Nigel, Dr. Sandra, Ms. Mirna
 EGO3: Ms. Mirna, Mr. Admin (permits for NPA), Dr. X (ecologist), Mr. Bugs (student)
 EGO4: Ms. Tutsi (user), Dr. Sandra
 EGO5: Dr. Nigel, Dr. Repsa, Mr. Green (International NGO), Mr. Admin, .... ??
