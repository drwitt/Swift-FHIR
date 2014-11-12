//
//  CompositionTests.swift
//  CompositionTests
//
//  Generated from FHIR 0.0.82.2943 on 2014-11-12.
//  2014, SMART Platforms.
//

import Cocoa
import XCTest
import SwiftFHIR


class CompositionTests: FHIRModelTestCase
{
	func instantiateFrom(filename: String) -> Composition? {
		let json = readJSONFile(filename)
		let instance = Composition(json: json)
		XCTAssertNotNil(instance, "Must have instantiated a test instance")
		return instance
	}
	
	func testComposition1() {
		let inst = instantiateFrom("composition-example.json")
		XCTAssertNotNil(inst, "Must have instantiated a Composition instance")
		
		XCTAssertEqual(inst!.attester![0].mode![0], "legal")	
		XCTAssertEqual(inst!.attester![0].party!.display!, "Robert Dolin MD")	
		XCTAssertEqual(inst!.attester![0].party!.reference!, "Practitioner/xcda-author")	
		XCTAssertEqual(inst!.author![0].display!, "Robert Dolin MD")	
		XCTAssertEqual(inst!.author![0].reference!, "Practitioner/xcda-author")	
		XCTAssertEqual(inst!.confidentiality!.code!, "1.3.6.1.4.1.21367.2006.7.101")	
		XCTAssertEqual(inst!.confidentiality!.display!, "Clinical-Staff")
		XCTAssertEqual(inst!.confidentiality!.system!, NSURL(string: "http://ihe.net/xds/connectathon/confidentialityCodes")!)	
		XCTAssertEqual(inst!.custodian!.display!, "Good Health Clinic")	
		XCTAssertEqual(inst!.custodian!.reference!, "Organization/2.16.840.1.113883.19.5")
		XCTAssertEqual(inst!.date!, NSDate.dateFromISOString("2012-01-04T09:10:14Z")!)
		XCTAssertEqual(inst!.identifier!.system!, NSURL(string: "http://healthintersections.com.au/test")!)	
		XCTAssertEqual(inst!.identifier!.value!, "1")	
		XCTAssertEqual(inst!.section![0].code!.coding![0].code!, "10164-2")
		XCTAssertEqual(inst!.section![0].code!.coding![0].system!, NSURL(string: "http://loinc.org")!)	
		XCTAssertEqual(inst!.section![0].content!.reference!, "MedicationAdministration/example")	
		XCTAssertEqual(inst!.section![0].title!, "History of present illness")	
		XCTAssertEqual(inst!.status!, "final")	
		XCTAssertEqual(inst!.subject!.display!, "Henry Levin the 7th")	
		XCTAssertEqual(inst!.subject!.reference!, "Patient/xcda")	
		XCTAssertEqual(inst!.text!.div!, "<div>\n      <p>Consultation note for Henry Levin the 7th</p>\n    </div>")	
		XCTAssertEqual(inst!.text!.status!, "generated")	
		XCTAssertEqual(inst!.type!.coding![0].code!, "11488-4")	
		XCTAssertEqual(inst!.type!.coding![0].display!, "Consult note")
		XCTAssertEqual(inst!.type!.coding![0].system!, NSURL(string: "http://loinc.org")!)
	}
}